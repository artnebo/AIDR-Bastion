import asyncio
from dataclasses import asdict

from app.modules.logger import pipeline_logger
from app.modules.opensearch import os_client
from app.pipelines.similarity_pipeline.const import INDEX_MAPPING, PROMPTS_EXAMPLES
from settings import get_settings

settings = get_settings()


async def create_index():
    """
    Create OpenSearch index for similarity rules with proper mapping.

    Returns:
        bool: True if index was created successfully, False otherwise
    """
    try:
        await os_client.connect()

        if await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            pipeline_logger.info(f"Index {os_client.similarity_prompt_index} already exists")
            return True

        await os_client.client.indices.create(index=os_client.similarity_prompt_index, body=INDEX_MAPPING)

        pipeline_logger.info(f"Index {os_client.similarity_prompt_index} created successfully")
        return True

    except Exception as e:
        pipeline_logger.error(f"Error creating index: {e}")
        return False
    finally:
        await os_client.close()


async def upload_prompts_examples():
    """
    Upload example prompts to the similarity rules index.

    Returns:
        bool: True if upload was successful, False otherwise
    """
    try:
        await os_client.connect()

        if not await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            pipeline_logger.info("Index does not exist, creating it first...")
            await os_client.close()
            if not await create_index():
                return False
            await os_client.connect()

        docs = [asdict(doc) for doc in PROMPTS_EXAMPLES]
        for doc in docs:
            await os_client.client.index(os_client.similarity_prompt_index, body=doc)

        pipeline_logger.info(f"Uploaded {len(docs)} example prompts to index")
        return True

    except Exception as e:
        pipeline_logger.error(f"Error uploading prompts: {e}")
        return False
    finally:
        await os_client.close()


async def check_index_exists() -> bool:
    """
    Check the status of the similarity rules index.

    Returns:
        dict: Index status information
    """
    try:
        await os_client.connect()

        if not await os_client.client.indices.exists(index=os_client.similarity_prompt_index):
            return False
        return True
    except Exception as e:
        pipeline_logger.error(f"Error checking index: {e}")
        return False
    finally:
        await os_client.close()


async def main():
    """
    Main function to create index and upload example prompts.
    """
    pipeline_logger.info("Starting index creation and data upload...")

    status = await check_index_exists()
    pipeline_logger.info(f"Current index exist: {'yes' if status else 'no'}")

    if await create_index():
        pipeline_logger.info("Index creation completed successfully")
    else:
        pipeline_logger.error("Failed to create index")
        return

    if await upload_prompts_examples():
        pipeline_logger.info("Data upload completed successfully")
    else:
        pipeline_logger.error("Failed to upload data")


if __name__ == "__main__":
    asyncio.run(main())
