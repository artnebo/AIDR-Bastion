# Usage

## Basic API Usage

```python
import requests

# Run pipeline analysis on a text prompt
response = requests.post("http://localhost:8000/api/v1/run_pipeline", json={
    "prompt": "Your text to analyze here",
    "pipeline_flow": "base"  # Must match a flow_name from config.json
})

result = response.json()
print(f"Status: {result['status']}")  # allow, block, or notify
print(f"Triggered rules: {result['result']}")

# Get available flows and pipelines
flows_response = requests.get("http://localhost:8000/api/v1/flows")
flows = flows_response.json()
print(f"Available flows: {[flow['flow_name'] for flow in flows['flows']]}")
```

## Python SDK Usage

```python
from app.manager import pipeline_manager

# Direct usage
result = await pipeline_manager.run_pipeline("Your prompt", "default")
print(f"Status: {result.status}")
for pipeline in result.pipelines:
    print(f"Pipeline: {pipeline.name}, Status: {pipeline.status}")
```

## Integration with Existing Applications

You can integrate project for your existing LLM application:

1. **Send requests:**
```python
import requests

def check_prompt_safety(prompt: str):
    response = requests.post(
        "http://localhost:8000/api/v1/run_pipeline",
        json={
            "prompt": prompt,
            "pipeline_flow": "security_audit"
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

2. **Configure your application to check all user inputs**
3. **Set up proper error handling and fallbacks**

## Project Configuration

The project can be configured through environment variables:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `CORS_ORIGINS`: Allowed origins for CORS
- `EMBEDDINGS_MODEL`: Hugging Face model for embeddings
- `SIMILARITY_NOTIFY_THRESHOLD`: Threshold for notifications
- `SIMILARITY_BLOCK_THRESHOLD`: Threshold for blocking

All required environments you can find in env.example
