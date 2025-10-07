# Usage

## Basic API Usage

```python
import requests

# Run pipeline analysis on a text prompt
response = requests.post("http://localhost:8000/api/v1/run_pipeline", json={
    "prompt": "Your text to analyze here",
    "pipeline_flow": "full_scan"
})

result = response.json()
print(f"Status: {result['status']}")  # allow, block, or notify
print(f"Triggered rules: {result['result']}")
```

## Python SDK Usage

```python
from app.manager import pipeline_manager

# Direct usage
result = await pipeline_manager.run_pipeline("Your prompt", "full_scan")
print(f"Status: {result.status}")
for pipeline in result.pipelines:
    print(f"Pipeline: {pipeline.name}, Status: {pipeline.status}")
```

## Integration Example

```python
def check_prompt_safety(prompt: str):
    response = requests.post(
        "http://localhost:8000/api/v1/run_pipeline",
        json={
            "prompt": prompt,
            "pipeline_flow": "full_scan"
        }
    )
    result = response.json()
    
    if result["status"] == "BLOCK":
        return False, "Prompt blocked"
    elif result["status"] == "NOTIFY":
        return True, "Prompt flagged but allowed"
    else:
        return True, "Prompt safe"
```