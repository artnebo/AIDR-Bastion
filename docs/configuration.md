# Configuration

## Environment Variables

The system can be configured through environment variables in the `.env` file:

```env
# FastAPI configuration
HOST=0.0.0.0
PORT=8000

# ML Pipeline
ML_MODEL_PATH=

# LLM Pipeline
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4
OPENAI_BASE_URL=https://api.openai.com/v1

# Similarity Pipeline
SIMILARITY_PROMPT_INDEX=similarity-prompt-index
SIMILARITY_NOTIFY_THRESHOLD=0.7
SIMILARITY_BLOCK_THRESHOLD=0.87

# OpenSearch configuration
OS__HOST=
OS__PORT=
OS__SCHEME=
OS__USER=
OS__PASSWORD=

# Kafka configuration
KAFKA__BOOTSTRAP_SERVERS=localhost:9092
KAFKA__TOPIC=aidr-events
KAFKA__SECURITY_PROTOCOL=PLAINTEXT

# Embeddings model
EMBEDDINGS_MODEL=
```

## Pipeline Configuration

The `config.json` file controls which Pipelines are active for each flow:

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
    }
]
```