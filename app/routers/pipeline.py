from fastapi import APIRouter

from app.manager import pipeline_manager
from app.models.pipeline import (
    FlowInfo,
    FlowsResponse,
    PipelineInfo,
    TaskRequest,
    TaskResult,
)

pipeline_router = APIRouter(prefix="/api/v1", tags=["pipeline"])


@pipeline_router.post("/run_pipeline")
async def run_pipeline(request: TaskRequest) -> TaskResult:
    task_result = await pipeline_manager.run_pipeline(prompt=request.prompt, pipeline_flow=request.pipeline_flow)
    return task_result


@pipeline_router.get("/flows")
async def get_flows() -> FlowsResponse:
    """
    Get list of all available flows and their pipelines.

    Returns:
        FlowsResponse: List of flows with pipeline information
    """
    flows = []

    for flow_name, pipelines in pipeline_manager.pipeline_flows.items():
        pipeline_infos = [PipelineInfo(name=pipeline.name, enabled=pipeline.enabled) for pipeline in pipelines]
        flows.append(FlowInfo(flow_name=flow_name, pipelines=pipeline_infos))

    return FlowsResponse(flows=flows)
