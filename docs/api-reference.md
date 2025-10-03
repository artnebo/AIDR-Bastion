# API Reference

## POST /api/v1/run_pipeline

Runs pipelines to analyze the input prompt.

**Request Body:**
```json
{
    "prompt": "string",
    "pipeline_flow": "string"  // Must match a flow_name from config.json
}
```

**Response:**
```json
{
    "status": "allow" | "block" | "notify",
    "result": [
        {
            "status": "allow" | "block" | "notify",
            "name": "string",
            "triggered_rules": [
                {
                    "id": "string",
                    "name": "string",
                    "details": "string",
                    "body": "string",
                    "action": "notify" | "block",
                    "severity": "string",
                    "cwe_id": "string"
                }
            ]
        }
    ]
}
```

## GET /api/v1/flows

Get a list of all available flows and their pipelines.

**Response:**
```json
{
    "flows": [
        {
            "flow_name": "string",
            "pipelines": [
                {
                    "name": "string",
                    "enabled": "boolean"
                }
            ]
        }
    ]
}
```
