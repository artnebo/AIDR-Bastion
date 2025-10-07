import asyncio
import sys
from dataclasses import asdict
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from app.modules.logger import pipeline_logger  # noqa: E402
from app.modules.opensearch import os_client  # noqa: E402
from app.pipelines.similarity_pipeline.const import INDEX_MAPPING, PROMPTS_EXAMPLES  # noqa: E402
from settings import get_settings  # noqa: E402
from app.utils import text_embedding  # noqa: E402

settings = get_settings()


async def create_index():
    """
    Create OpenSearch index for similarity rules with proper mapping.

    Returns:
        bool: True if index was created successfully, False otherwise
    """
    try:

        if await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            pipeline_logger.info(f"Index {os_client.similarity_prompt_index} already exists")
            return True

        await os_client.client.indices.create(index=os_client.similarity_prompt_index, body=INDEX_MAPPING)

        pipeline_logger.info(f"Index {os_client.similarity_prompt_index} created successfully")
        return True

    except Exception as e:
        pipeline_logger.error(f"Error creating index: {e}")
        return False


async def upload_prompts_examples():
    """
    Upload example prompts to the similarity rules index.

    Returns:
        bool: True if upload was successful, False otherwise
    """
    try:

        if not await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            pipeline_logger.info("Index does not exist, creating it first...")
            await os_client.close()
            if not await create_index():
                return False

        docs = [asdict(doc) for doc in PROMPTS_EXAMPLES]
        for doc in docs:
            doc["vector"] = text_embedding(doc["text"])
            await os_client.client.index(os_client.similarity_prompt_index, body=doc)

        pipeline_logger.info(f"Uploaded {len(docs)} example prompts to index")
        return True

    except Exception as e:
        pipeline_logger.error(f"Error uploading prompts: {e}")
        return False


async def check_index_exists() -> bool:
    """
    Check the status of the similarity rules index.

    Returns:
        dict: Index status information
    """
    try:
        if not await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            return False
        return True
    except Exception as e:
        pipeline_logger.error(f"Error checking index: {e}")
        return False


async def main():
    """
    Main function to create index and upload example prompts.
    """
    pipeline_logger.info("Starting index creation and data upload...")

    try:
        status = await check_index_exists()
        pipeline_logger.info(f"Current index exist: {'yes' if status else 'no'}")

        if not status:
            if await create_index():
                pipeline_logger.info("Index creation completed successfully")
            else:
                pipeline_logger.error("Failed to create index")
                return

        if await upload_prompts_examples():
            pipeline_logger.info("Data upload completed successfully")
        else:
            pipeline_logger.error("Failed to upload data")
    finally:
        await os_client.close()


if __name__ == "__main__":
    asyncio.run(main())
