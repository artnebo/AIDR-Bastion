from opensearchpy import (
    AsyncOpenSearch,
    ConnectionError,
    OpenSearchException,
    RequestError,
)

from app.modules.logger import pipeline_logger
from settings import OpenSearchSettings, get_settings


class AsyncOpenSearchClient:
    """
    Asynchronous client for working with OpenSearch.

    This class provides functionality for connecting to OpenSearch, executing search queries
    and working with vectors for finding similar documents. Supports automatic reconnection
    and error handling with detailed logging.

    Attributes:
        _client (AsyncOpenSearch): Asynchronous OpenSearch client
        _os_settings (OpenSearchSettings): OpenSearch connection settings
        similarity_prompt_index (str): Index name for searching similar prompts
    """

    _client: AsyncOpenSearch

    def __init__(self, os_settings: OpenSearchSettings, similarity_prompt_index: str) -> None:
        """
        Initializes OpenSearch client with connection settings.

        Args:
            os_settings (OpenSearchSettings): Settings for connecting to OpenSearch
        """
        self._os_settings = os_settings
        self.similarity_prompt_index = similarity_prompt_index
        self._client = AsyncOpenSearch(
            hosts=[{"host": self._os_settings.host, "port": self._os_settings.port}],
            scheme=self._os_settings.scheme,
            http_auth=(self._os_settings.user, self._os_settings.password),
            use_ssl=True,
            verify_certs=False,
            ssl_show_warn=False,
            retry_on_status=(500, 502, 503, 504),
            retry_on_timeout=True,
            timeout=30,
            pool_maxsize=self._os_settings.pool_size,
            max_retries=3,
        )

    @property
    def client(self) -> AsyncOpenSearch:
        """
        Returns current OpenSearch client.

        Returns:
            AsyncOpenSearch: Asynchronous OpenSearch client

        Raises:
            AttributeError: If client is not initialized
        """
        return self._client

    async def check_connection(self) -> None:
        """
        Establishes connection with OpenSearch server.

        Creates asynchronous connection to OpenSearch, configures connection parameters
        and checks server availability. Logs errors if connection fails.

        Raises:
            Exception: On failed connection or OpenSearch error
        """
        if not self._os_settings:
            return
        try:
            is_connected = await self._client.ping()
            if not is_connected:
                raise Exception("Failed to connect to OpenSearch")
        except Exception as e:
            error_msg = f"Failed to connect to OpenSearch. Error: {str(e)}"
            pipeline_logger.exception(f"[{self._os_settings.host}] {error_msg}")
            self._client = None

    async def close(self) -> None:
        """
        Closes connection with OpenSearch server.

        Closes connection pool and cleans up client resources. Logs errors
        if connection closing fails.

        Raises:
            Exception: On connection closing error
        """
        try:
            if self._client:
                await self._client.close()
                self._client = None
        except OpenSearchException as e:
            error_msg = f"Failed to close pool of connections to OpenSearch. Error: {e}"
            pipeline_logger.exception(f"[{self._os_settings.host}] {error_msg}")

    async def _search(self, index: str, body: dict) -> dict | None:
        """
        Executes search query to OpenSearch.

        Private method for executing search queries to specified index.
        Handles connection and query errors with detailed logging.

        Args:
            index (str): Index name for search
            body (dict): Search query body

        Returns:
            dict | None: Search query result from OpenSearch, or None if error occurred

        Raises:
            Exception: On connection error or invalid query
        """
        try:
            return await self._client.search(index=index, body=body)
        except ConnectionError as e:
            error_msg = f"Failed to establish connection with OpenSearch. Error: {e}"
            pipeline_logger.error(f"[{self._os_settings.host}][{index}] {error_msg}")
            return None
        except RequestError as e:
            error_msg = f"OpenSearch Response Error: Bad Request. Error: {e}"
            pipeline_logger.exception(f"[{self._os_settings.host}] {error_msg}")
            return None
        except Exception as e:
            error_msg = f"Failed to execute search query. Error: {e}"
            pipeline_logger.exception(f"[{self._os_settings.host}][{index}] {error_msg}")
            return None

    async def search_similar_documents(self, vector: list[float]) -> list[dict]:
        """
        Searches for similar documents by vector using cosine similarity.

        Performs search for documents similar to given vector using
        cosine similarity. Returns up to 5 most similar documents, grouping
        them by categories to avoid duplicates.

        Args:
            vector (list[float]): Vector for searching similar documents

        Returns:
            list[dict]: List of similar documents, grouped by categories.
                       Each document contains metadata and source data.
        """
        if not vector or not isinstance(vector, list) or len(vector) == 0:
            pipeline_logger.warning(
                f"[{self._os_settings.host}][{self.similarity_prompt_index}] Invalid vector provided for similarity search"
            )
            return []

        # Check if vector has expected dimensions (typically 768 for many embedding models)
        if len(vector) != 768:
            pipeline_logger.warning(
                f"[{self._os_settings.host}][{self.similarity_prompt_index}] Vector dimension mismatch: expected 768, got {len(vector)}"
            )

        # Use KNN query for vector similarity search
        body = {"size": 5, "query": {"knn": {"vector": {"vector": vector, "k": 5}}}}

        # Log the query for debugging
        pipeline_logger.debug(
            f"[{self._os_settings.host}][{self.similarity_prompt_index}] Executing similarity search with vector length: {len(vector)}"
        )
        pipeline_logger.debug(f"[{self._os_settings.host}][{self.similarity_prompt_index}] Query body: {body}")
        try:
            # Check if index exists before searching
            if not await self._client.indices.exists(index=self.similarity_prompt_index):
                pipeline_logger.warning(
                    f"[{self._os_settings.host}][{self.similarity_prompt_index}] Index does not exist"
                )
                return []
        except Exception as e:
            pipeline_logger.error(
                f"[{self._os_settings.host}][{self.similarity_prompt_index}] Failed to check index existence: {e}"
            )
            return []

        resp = await self._search(index=self.similarity_prompt_index, body=body)
        if resp:
            documents = {}
            for hit in resp.get("hits", {}).get("hits", []):
                if hit["_source"]["category"] not in documents:
                    documents[hit["_source"]["category"]] = hit
            return list(documents.values())

        # Fallback: try simpler KNN query if the main one failed
        pipeline_logger.warning(
            f"[{self._os_settings.host}][{self.similarity_prompt_index}] Main KNN query failed, trying fallback"
        )
        fallback_body = {"size": 5, "query": {"knn": {"vector": {"vector": vector, "k": 3}}}}

        fallback_resp = await self._search(index=self.similarity_prompt_index, body=fallback_body)
        if fallback_resp:
            documents = {}
            for hit in fallback_resp.get("hits", {}).get("hits", []):
                if hit["_source"]["category"] not in documents:
                    documents[hit["_source"]["category"]] = hit
            return list(documents.values())

        pipeline_logger.error(
            f"[{self._os_settings.host}][{self.similarity_prompt_index}] Failed to search similar documents - no response from OpenSearch"
        )
        return []

    async def test_connection(self) -> bool:
        """
        Test OpenSearch connection and basic functionality.

        Returns:
            bool: True if connection is working, False otherwise
        """
        try:
            # Test basic ping
            if not await self._client.ping():
                return False

            # Test index existence
            if not await self._client.indices.exists(index=self.similarity_prompt_index):
                pipeline_logger.warning(
                    f"[{self._os_settings.host}][{self.similarity_prompt_index}] Index does not exist for testing"
                )
                return False

            # Test simple query
            test_body = {"size": 1, "query": {"match_all": {}}}

            resp = await self._search(index=self.similarity_prompt_index, body=test_body)
            if resp:
                pipeline_logger.info(
                    f"[{self._os_settings.host}][{self.similarity_prompt_index}] Connection test successful"
                )
                return True
            else:
                pipeline_logger.error(
                    f"[{self._os_settings.host}][{self.similarity_prompt_index}] Connection test failed - no response"
                )
                return False

        except Exception as e:
            pipeline_logger.error(
                f"[{self._os_settings.host}][{self.similarity_prompt_index}] Connection test failed: {e}"
            )
            return False


try:
    os_client: AsyncOpenSearchClient = AsyncOpenSearchClient(
        os_settings=get_settings().OS, similarity_prompt_index=get_settings().SIMILARITY_PROMPT_INDEX
    )
except Exception as e:
    pipeline_logger.error(f"Failed to create OpenSearch client: {e}")
    os_client = None
