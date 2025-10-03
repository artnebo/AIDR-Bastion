# Development

## Setting up OpenSearch

1. **Install OpenSearch**
   ```bash
   docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" opensearchproject/opensearch:latest
   ```

2. **Create similarity index**
   ```bash
   python app/pipelines/similarity_pipeline/index_script.py
   ```
   
   This will create the `similarity-prompt-index` index in OpenSearch. You can customize the index name by setting the SIMILARITY_PROMPT_INDEX environment variable.

## Setting up Kafka for Event Logging

AIDR Bastion supports Kafka integration for logging BLOCK and NOTIFY events, enabling scalable event streaming and real-time monitoring.

### Quick Start with Docker Compose

**Configure environment variables**
Minimal required environments
```bash
# Add to your .env file
KAFKA__BOOTSTRAP_SERVERS=localhost:9092
KAFKA__TOPIC=aidr-events
KAFKA__SECURITY_PROTOCOL=PLAINTEXT
```

Full Kafka environment variables
```bash
## Kafka configuration
# KAFKA__BOOTSTRAP_SERVERS=
# KAFKA__TOPIC=
# KAFKA__SECURITY_PROTOCOL=PLAINTEXT
# KAFKA__SASL_MECHANISM=
# KAFKA__SASL_USERNAME=
# KAFKA__SASL_PASSWORD=
# KAFKA__SAVE_PROMPT=true 
```

The environment variable `KAFKA__SAVE_PROMPT` is optional. It controls whether the input prompt data should be saved to Kafka or not.

### Event Logging Features

- **BLOCK Events**: Logged when prompts are blocked by detection rules
- **NOTIFY Events**: Logged when prompts trigger notifications but are allowed
- **Structured JSON**: Events include prompt content, detection results, and metadata
- **Real-time Streaming**: Events are sent immediately to Kafka topics

### Event Schema

```json
{
	"status": "block",
	"pipelines": [
		{
			"status": "block",
			"name": "Pipeline Name",
			"triggered_rules": [
				{
					"details": "",
					"action": "block",
					"id": "a12d86d8-d96a-41fa-9e9a-18231539cfde",
					"name": "Instruction Overriding",
					"severity": null,
					"cwe_id": null
				}
			]
		}
	],
	"service": "AIDR Bastion",
	"version": "1.0.0",
	"timestamp": "2025-09-24T14:39:50.351466",
	"task_id": 1 // unique identifier passed through endpoint run_pipeline
}
```

### Advanced Kafka Configuration

For production environments, configure additional security settings:

```bash
# SASL Authentication
KAFKA__SECURITY_PROTOCOL=SASL_SSL
KAFKA__SASL_MECHANISM=PLAIN
KAFKA__SASL_USERNAME=your_username
KAFKA__SASL_PASSWORD=your_password

# SSL Configuration (if required)
KAFKA__SSL_CA_LOCATION=/path/to/ca-cert
KAFKA__SSL_CERTIFICATE_LOCATION=/path/to/client-cert
KAFKA__SSL_KEY_LOCATION=/path/to/client-key
```

## Rule Management
- **test_rules.py**: Comprehensive rule testing and validation
- **generate_rules.py**: Interactive rule creation and conversion
- **[Roota](https://github.com/UncoderIO/Roota)**: Public-domain language for collective cyber defense
- **[Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**: Convert Roota/Sigma rules to Semgrep format
- **[SOC Prime](https://socprime.com/)**: Access comprehensive threat detection rules
