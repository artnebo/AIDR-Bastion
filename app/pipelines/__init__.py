from app.pipelines.llm_pipeline.pipeline import LLMPipeline
from app.pipelines.ml_pipeline.pipeline import MLPipeline
from app.pipelines.regex_pipeline.pipeline import RegexPipeline
from app.pipelines.code_analysis_pipeline.pipeline import CodeAnalysisPipeline
from app.pipelines.similarity_pipeline.pipeline import SimilarityPipeline

__PIPELINES__ = [
    SimilarityPipeline(),
    CodeAnalysisPipeline(),
    RegexPipeline(),
    MLPipeline(),
    LLMPipeline(),
]


ENABLED_PIPELINES_MAP = {pipeline.name: pipeline for pipeline in __PIPELINES__ if pipeline.enabled}
PIPELINES_MAP = {pipeline.name: pipeline for pipeline in __PIPELINES__}
