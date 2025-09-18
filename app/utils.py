"""
Module for managing pipelines and their configuration.
Moved to a separate file to avoid circular imports.
"""

from typing import TYPE_CHECKING, Optional

import ollama
from sentence_transformers import SentenceTransformer

from app.modules.logger import pipeline_logger
from settings import get_settings

if TYPE_CHECKING:
    from app.pipelines.base import BasePipeline


settings = get_settings()

model = None
if settings.EMBEDDINGS_MODEL:
    try:
        model = SentenceTransformer(settings.EMBEDDINGS_MODEL, trust_remote_code=True, revision="main")
    except Exception as e:
        pipeline_logger.error(f"Failed to load embeddings model: {e}")
        model = None


def get_pipelines_from_config(configs: list[dict]) -> dict[str, list["BasePipeline"]]:
    """
    Converts pipeline configuration from names to pipeline instances.

    Args:
        configs: List of dictionaries with pipeline configuration (names as strings)

    Returns:
        Dictionary with categories and pipeline instances
    """
    # Import here to avoid circular imports
    from app.pipelines import PIPELINES_MAP

    result = {}

    for config in configs:
        pipelines = []
        flow_name = config.get("pipeline_flow")
        for pipeline_name in config.get("pipelines"):
            try:
                pipelines.append(PIPELINES_MAP[pipeline_name])
            except KeyError:
                pipeline_logger.error(f"Pipeline {pipeline_name} not found in PIPELINES_MAP")
        if flow_name and pipelines:
            result[flow_name] = pipelines
    result["default"] = list(PIPELINES_MAP.values())
    return result


def ollama_text_embedding(text: str) -> Optional[list[float]]:
    """
    Generate vector embedding for the given text using Ollama model.

    This function converts text into a numerical vector representation that can be used
    for similarity comparisons and vector-based operations. The embedding is generated
    using the configured Ollama model and is expected to be 768-dimensional.

    Args:
        text: The input text to generate embedding for

    Returns:
        Optional[list[float]]: A list containing the 768-dimensional embedding vector,
                              or None if embedding generation fails or returns invalid data

    Raises:
        ValueError: If the received embedding is None or doesn't have the expected 768 dimensions

    Note:
        The function expects the embedding model to return vectors with exactly 768 dimensions.
        If the model returns a different dimension count, the function will raise a ValueError.
    """
    embeddings_model = settings.EMBEDDINGS_MODEL
    if not embeddings_model:
        raise ValueError("EMBEDDINGS_MODEL is not set")
    try:
        response = ollama.embeddings(model=embeddings_model, prompt=text)
        embedding = response.get("embedding")
        if embedding is None or len(embedding) != 768:
            raise ValueError(f"Invalid embedding received for text: {text}")
        return [embedding]
    except Exception as err:
        pipeline_logger.error(f"Error generating embedding for text: {text}, error={str(err)}")


def text_embedding(prompt: str) -> list[float]:
    """
    Create vector embedding from text prompt.

    Args:
        prompt: Text to convert to vector

    Returns:
        List of float values representing the vector
    """
    if model is None:
        raise ValueError("Embeddings model is not loaded. Please check EMBEDDINGS_MODEL setting.")
    return model.encode(prompt, normalize_embeddings=True).tolist()
