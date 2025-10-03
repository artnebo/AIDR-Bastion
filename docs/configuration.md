# Configuration

## Environment Variables (.env)

```env
# FastAPI configuration
HOST=0.0.0.0
PORT=8000


# ML Pipeline. 
# Path to the model
ML_MODEL_PATH=

# LLM Pipeline
# model by default gpt-4
OPENAI_API_KEY=
OPENAI_MODEL=
OPENAI_BASE_URL=

# Similarity Pipeline
# similarity-prompt-index by default
SIMILARITY_PROMPT_INDEX=

SIMILARITY_NOTIFY_THRESHOLD=0.7
SIMILARITY_BLOCK_THRESHOLD=0.87

# OpenSearch configuration
OS__HOST=
OS__PORT=
OS__SCHEME=
OS__USER=
OS__PASSWORD=

# Kafka configuration (for event logging)
KAFKA__BOOTSTRAP_SERVERS=localhost:9092
KAFKA__TOPIC=aidr-events
KAFKA__SECURITY_PROTOCOL=PLAINTEXT
KAFKA__SASL_MECHANISM=
KAFKA__SASL_USERNAME=
KAFKA__SASL_PASSWORD=

# requires for creating embedding in pipelines: Similarity Pipeline and ML Pipeline
EMBEDDINGS_MODEL=

## Kafka configuration
# KAFKA__BOOTSTRAP_SERVERS=
# KAFKA__TOPIC=
# KAFKA__SECURITY_PROTOCOL=PLAINTEXT
# KAFKA__SASL_MECHANISM=
# KAFKA__SASL_USERNAME=
# KAFKA__SASL_PASSWORD=
# KAFKA__SAVE_PROMPT=true 
```

## Pipeline Configuration (config.json)

The `config.json` file controls which Pipelines are active for each flow.
Default `config.json` configuraton:

```json
[
    {
        "pipeline_flow": "full_scan",
        "pipelines": [
            "similarity",
            "regex",
            "openai",
            "ml",
            "code_analysis"
        ]
    },
    {
        "pipeline_flow": "code_audit",
        "pipelines": [
            "code_analysis"
        ]
    },
    {
        "pipeline_flow": "model_audit",
        "pipelines": [
            "ml",
            "openai"
        ]
    },
    {
        "pipeline_flow": "base_audit",
        "pipelines": [
            "regex",
            "similarity"
        ]
    }
]
```

### Configuration Impact

- **Flow names**: Can be any custom name (e.g., `base`, `code`, `security`, `content`). The name must match what you pass in the API request's `pipeline_flow` parameter
- **Pipeline names**: Must match the Pipeline names defined in `PipelineNames` enum
- **Order matters**: Pipelines run in the order specified in the array
- **Example flows**:
  - `base` flow: Pipelines general text prompts for harmful content
  - `code` flow: Pipelines code snippets for security vulnerabilities
  - `custom_flow`: You can create any custom flow name for specific use cases
