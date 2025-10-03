# Adding Custom Pipelines

## Step 1: Create Pipeline Class

```python
# app/pipelines/my_pipeline/pipeline.py
from app.pipelines.base import BasePipeline
from app.core.enums import PipelineNames, ActionStatus
from app.models.pipeline import PipelineResult, TriggeredRuleData

class MyCustomPipeline(BasePipeline):
    name = PipelineNames.my_pipeline
    enabled = True

    async def run(self, prompt: str, **kwargs) -> PipelineResult:
        # Your analyzing logic here
        triggered_rules = []
        
        # Example: Check for specific patterns
        if "malicious_pattern" in prompt.lower():
            triggered_rules.append(TriggeredRuleData(
                id="my_rule_1",
                name="Malicious Pattern Detected",
                details="Found potentially malicious content",
                body=prompt,
                action=RuleAction.BLOCK
            ))

        status = ActionStatus.BLOCK if triggered_rules else ActionStatus.ALLOW
        return PipelineResult(
            name=self.name,
            status=status,
            triggered_rules=triggered_rules
        )
```

## Step 2: Register Pipeline

```python
# app/pipelines/__init__.py
from app.pipelines.my_pipeline.pipeline import MyCustomPipeline

__PIPELINES__ = [
    # ... existing pipelines
    MyCustomPipeline(),
]

PIPELINES_MAP = {
    pipeline.name: pipeline for pipeline in __PIPELINES__
    if pipeline.enabled
}
```

## Step 3: Add to Configuration

```json
[
    {
        "flow_name": "base",
        "pipelines": [
            "personal_info",
            "similarity",
            "regex",
            "my_pipeline"
        ]
    }
]
```

## Step 4: Add Pipeline Name to Enum

```python
# app/core/enums.py
class PipelineNames(str, Enum):
    # ... existing names
    my_pipeline = "my_pipeline"
```
