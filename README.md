<<<<<<< HEAD
# AIDR Bastion Documentation Website

Official documentation website for AIDR Bastion - A comprehensive GenAI protection system.

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Local Development

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

```bash
npm run deploy
```

## 📁 Project Structure

```
AIDR-Bastion-site/
├── docs/                      # Markdown documentation
│   ├── intro.md
│   ├── installation.md
│   ├── pipelines/
│   └── rules/
├── src/
│   ├── pages/                 # React pages
│   │   ├── index.tsx         # Homepage
│   │   └── index.module.css
│   └── css/                   # Global styles
│       └── custom.css
├── static/                    # Static assets
│   └── img/
├── docusaurus.config.js      # Site configuration
├── sidebars.js              # Sidebar navigation
└── package.json
```

## 🎨 Design Theme

### Cyberpunk Neon Style

This site features a custom cyberpunk-inspired design with:
- 🏰 **3D Logo**: Custom isometric fortress with neon AIDR branding
- 💚 **Neon Green Effects**: Glowing lines, animations, and accents
- 🌊 **Abstract Animations**: Flowing neon lines across backgrounds
- 🎯 **Modern UI**: Cards, badges, and buttons with glow effects

### Color Scheme

Edit `src/css/custom.css` for color customization:

```css
:root {
  --ifm-color-primary: #00ff88;           /* Neon Green */
  --ifm-background-color: #292C3D;        /* Dark Blue-Gray */
  --ifm-background-surface-color: #2f3349;
  --ifm-code-background: #242838;
}
```

### Key Files

- **Homepage**: `src/pages/index.tsx` - Hero section with animations
- **Homepage Styles**: `src/pages/index.module.css` - Neon effects and animations
- **Global Styles**: `src/css/custom.css` - Color scheme and variables
- **Documentation**: `docs/*.md` - Markdown content
- **Navigation**: `sidebars.js` - Sidebar configuration
- **Logo**: `static/img/aidr-bastion-logo.png` - 3D cyberpunk fortress

## 📚 Documentation

For more information about Docusaurus, visit:
- [Docusaurus Documentation](https://docusaurus.io/)
- [AIDR Bastion Repository](https://github.com/0xAIDR/AIDR-Bastion)

## 📝 License

Documentation is licensed under [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html).

AIDR Bastion project is licensed under [LGPL-3.0](https://github.com/0xAIDR/AIDR-Bastion/blob/main/LICENSE).



=======
# AIDR Bastion

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)](LICENSE)

A comprehensive GenAI protection system designed to safeguard against malicious prompts, injection attacks, and harmful content. The system incorporates multiple detection engines that operate sequentially to analyze and classify user inputs before reaching GenAI applications.

- The system supports [Roota](https://github.com/UncoderIO/Roota) and [Sigma rules](https://sigmahq.io/docs/guide/about.html), enabling the application of detection logic from multiple sources such as [SigmaHQ](https://github.com/SigmaHQ/sigma) (around 1,200 compatible free community Sigma rules available at release), [SOC Prime](https://tdm.socprime.com/) (with up to 3,000 additional compatible rules), and other third-party repositories. Sigma rules can be applied to detect use cases where malware leverages a local LLM to generate malicious code for execution.
- SOC Prime [Uncoder AI](https://tdm.socprime.com/uncoder-ai/) integration further extends functionality by translating Sigma rules into Semgrep format, providing standardized and reusable detection pipelines (requires a free account).
- Roota rules power the regex-based pipeline.
- The architecture supports rule extensibility, seamlessly integrating organization-specific signatures and external detection content.
- The system can also function as a local logging sensor, recording user and agent prompts and enabling diagnostics, incident discovery, and cyber attack investigation.
- Detection logic aligns with industry frameworks such as [MITRE ATLAS](https://atlas.mitre.org/) and [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/), ensuring standardized coverage against adversarial techniques.
- Actions include allow, block, or notify, depending on rule matches and policy configuration.

This layered detection approach delivers defense-in-depth against evolving adversarial prompt engineering and other AI-focused attack vectors.
Inspired by LlamaFirewall.

## 🚀 Features

- **Multi-Pipeline Detection**: Regex patterns, ML models, vector-based similarity detection, and LLM-based analysis
- **Flexible Configuration**: Dynamic Pipeline configuration via JSON
- **Real-time Analysis**: Fast async processing with configurable thresholds
- **OpenSearch Integration**: Vector-based similarity search for prompt classification
- **RESTful API**: Easy integration with existing applications
- **Extensible Architecture**: Simple plugin system for custom Pipelines

## 🏗️ Architecture

```
┌────────────────────────────────┐
│   FastAPI Endpoint             │
│   (POST /api/v1/run_pipeline)  │
└──────────────┬─────────────────┘
               │
               ▼
      ┌─────────────────────┐
      │  Pipeline Manager   │
      └─────────┬───────────┘
                │
                ▼
      ┌──────────────────────────────┐
      │          Pipelines           │
      │ ┌──────────────────────────┐ │
      │ │  Regex Pipeline          │ │
      │ ├──────────────────────────┤ │
      │ │  Similarity Pipeline     │ │
      │ ├──────────────────────────┤ │
      │ │  Code Analysis Pipeline  │ │
      │ ├──────────────────────────┤ │
      │ │  ML Pipeline             │ │
      │ ├──────────────────────────┤ │
      │ │  LLM (OpenAI) Pipeline   │ │
      │ └──────────────────────────┘ │
      └──────────────────────────────┘

```

## 📋 Table of Contents

- [Installation](#%EF%B8%8F-installation)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Pipelines](#-pipelines)
- [Rule Management and Customization](#-rule-management-and-customization)
- [Adding Custom Pipelines](#-adding-custom-pipelines)
- [Development](#-development)
- [License](#-license)
- [Built With](#%EF%B8%8F-built-with)
- [TO-DO List](#%EF%B8%8F-to-do-list)

## 🛠️ Installation

### Prerequisites

- Python 3.12+
- OpenSearch (for Similarity Pipeline)
- OpenAI API key (for LLM Pipeline)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/0xAIDR/AIDR-Bastion.git
   cd AIDR-Bastion
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python server.py
   ```

By default, the API will be available at `http://localhost:8000`. You can customize the host and port using the HOST and PORT environment variables.

## ⚙️ Configuration

### Environment Variables (.env)

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

### Pipeline Configuration (config.json)

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

#### Configuration Impact

- **Flow names**: Can be any custom name (e.g., `base`, `code`, `security`, `content`). The name must match what you pass in the API request's `pipeline_flow` parameter
- **Pipeline names**: Must match the Pipeline names defined in `PipelineNames` enum
- **Order matters**: Pipelines run in the order specified in the array
- **Example flows**:
  - `base` flow: Pipelines general text prompts for harmful content
  - `code` flow: Pipelines code snippets for security vulnerabilities
  - `custom_flow`: You can create any custom flow name for specific use cases

## 🚀 Usage

### Basic API Usage

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

### Python SDK Usage

```python
from app.manager import pipeline_manager

# Direct usage
result = await pipeline_manager.run_pipeline("Your prompt", "default")
print(f"Status: {result.status}")
for pipeline in result.pipelines:
    print(f"Pipeline: {pipeline.name}, Status: {pipeline.status}")
```

### Integration with Existing Applications

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

### Project Configuration

The project can be configured through environment variables:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `CORS_ORIGINS`: Allowed origins for CORS
- `EMBEDDINGS_MODEL`: Hugging Face model for embeddings
- `SIMILARITY_NOTIFY_THRESHOLD`: Threshold for notifications
- `SIMILARITY_BLOCK_THRESHOLD`: Threshold for blocking

All required environments you can find in env.example

## 📚 API Reference

### POST /api/v1/run_pipeline

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

### GET /api/v1/flows

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

## 🔍 Pipelines

### 1. Regex Pipeline (`regex`)
- **Purpose**: Pattern-based detection using regular expressions
- **Rules**: YAML files in `app/pipelines/regex_pipeline/rules/`
- **Categories**: 
  - **Injection**: SQL, command execution, path traversal
  - **Obfuscation**: Character obfuscation, encoding, Unicode homoglyphs
  - **Override**: Role play, filter disabling, context splicing
  - **Leakage**: Direct prompt requests, forced repetition
  - **PII**: Email, phone, credit cards, passwords, API keys, UUIDs, IBAN
  - **Semantic**: Emotional manipulation, authority fallacy, multilingual attacks
  - **DoS**: Character/word repetition, regex DoS
- **Best for**: Known attack patterns and simple text analysis

### 2. Similarity Pipeline (`similarity`)
- **Purpose**: Vector-based similarity detection against known harmful prompts
- **Backend**: OpenSearch with vector search
- **Required**: OpenSearch configuration
- **Configuration**: `SIMILARITY_NOTIFY_THRESHOLD`, `SIMILARITY_BLOCK_THRESHOLD`
- **Best for**: Detecting variations of known attacks

### 3. Code Analysis Pipeline (`code_analysis`)
- **Purpose**: Static code analysis using Semgrep
- **Languages**: Python, JavaScript, Java, C++, and more
- **Rules**: Security-focused patterns
- **Best for**: Code injection and vulnerability detection

### 4. ML Pipeline (`ml`)
- **Purpose**: Machine learning-based classification
- **Configuration**: Requires `ML_PIPELINE_PATH`
- **Model**: Custom-trained model for prompt classification
- **Best for**: General malicious content detection
- **Required**: Configured environment `EMBEDDINGS_MODEL`

### 5. LLM Pipeline (`openai`)
- **Purpose**: AI-powered analysis using OpenAI GPT models
- **Configuration**: Requires `OPENAI_API_KEY` and `OPENAI_MODEL` (default is gpt-4). The `OPENAI_BASE_URL` environment variable is optional; by default, it is set to https://api.openai.com/v1
- **Features**: JSON response format, configurable models, intelligent decision-making
- **Response Format**: Returns structured JSON with status (block/notify/allow) and reasoning
- **Best for**: Complex reasoning and context-aware analysis

## 📋 Rule Management and Customization

### YAML Rules for Regex Pipeline

The Regex Pipeline defines detection patterns using [Roota](https://github.com/UncoderIO/Roota) rules files. Roota is a public-domain language for collective cyber defense that combines native queries from SIEM, EDR, XDR, or Data Lake with standardized metadata and threat intelligence to enable automated translation into other languages.

Each rule file follows a specific structure:

```yaml
name: "Rule Name"
description: "Description of what this rule detects"
severity: "high|medium|low"
category: "injection|obfuscation|override|leakage|pii|semantic|dos"
patterns:
  language: llm-regex-pattern
  pattern: 
   - "pattern"
   - "another_pattern"
action: "block|notify|allow"
```

**Rule Categories:**
- **Injection**: SQL injection, command execution, path traversal, script injection
- **Obfuscation**: Character obfuscation, encoding tricks, Unicode homoglyphs
- **Override**: Role play attacks, filter disabling, context splicing
- **Leakage**: Direct prompt requests, forced repetition attacks
- **PII**: Personal identifiable information detection (emails, phones, credit cards, etc.)
- **Semantic**: Emotional manipulation, authority fallacy, multilingual attacks
- **DoS**: Denial of service patterns (character repetition, regex DoS)

### Semgrep Rules for Code Analysis Pipeline

The code pipeline uses Semgrep rules for static code analysis. Rules are located in `app/pipelines/semgrep_pipeline/rules/`.

**Rule Structure:**
```yaml
rules:
  - id: rule-id
    message: "Security issue description"
    languages: [python, javascript, java]
    severity: ERROR
    patterns:
      - pattern: |
          $PATTERN
    fix: |
      $FIX
```

### Managing Rules

#### Using Roota for Rule Creation

[Roota](https://github.com/UncoderIO/Roota) is a public-domain language for collective cyber defense that provides:

- **YAML-based format** that's easy to write and human-readable
- **Multi-language support** for SIEM, EDR, XDR, and Data Lake queries
- **MITRE ATT&CK mapping** for threat intelligence integration
- **Threat actor timeline** support for coordinated defense
- **Correlation support** for more robust detection logic
- **OCSF and Sigma compatibility** for maximum compatibility

**Roota Rule Example:**
```yaml
name: 'INJ-001: SQL Keywords'
details: Detects common SQL manipulation keywords. Designed to be a high-confidence signal. https://tdm.socprime.com/
author: SOC Prime Team
severity: critical
date: 2025-08-08
logsource:
  product: llm
  service: firewall
  module: regex
detection:
  language: llm-regex-pattern
  pattern:
    - '(?i)\b(?:SELECT\s+(?:(?!\bFROM\b)[^,;]+,)+(?:(?!\bFROM\b)[^,;]+)\s+FROM|INSERT\s+INTO|UPDATE\s+[\w\.]+\s+SET|DELETE\s+FROM|DROP\s+(?:TABLE|DATABASE)|ALTER\s+TABLE|CREATE\s+TABLE|TRUNCATE\s+TABLE)\b'
references:
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://owasp.org/Top10/A03_2021-Injection/
license: DRL 1.1
uuid: f1a2b3c4-d5e6-4f7a-8b8c-9d0e1f2a3b4c
response: block
```

#### Using Uncoder AI for Semgrep Rules

[Uncoder AI](https://tdm.socprime.com/uncoder-ai/) is a powerful tool for converting Sigma and Roota rules to various formats including Semgrep:

1. **Visit [Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**
2. **Register account for free**
3. **Select Roota/Sigma to Semgrep conversion**
4. **Paste your Roota or Sigma rule**
5. **Generate Semgrep YAML rule**
6. **Save the generated rule** in `app/pipelines/semgrep_pipeline/rules/`

**Example Sigma Rule:**
```yaml
title: Suspicious PowerShell Command
description: Detects suspicious PowerShell commands
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    - CommandLine: '*powershell*'
    - CommandLine: '*Invoke-Expression*'
  condition: selection
```

#### Using SOC Prime for Advanced Rules

[SOC Prime](https://tdm.socprime.com/) provides comprehensive threat detection rules including Roota and Sigma formats:

1. **Visit [SOC Prime](https://tdm.socprime.com/)**
2. **Browse the Rules Library** (Sigma, Roota, and other formats)
3. **Filter by technology and threat type**
4. **Download or convert rules using [Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**
5. **Adapt rules for your specific use case**

### Custom Rule Development

#### Creating Custom Regex Rules

1. **Identify the attack pattern**
2. **Create YAML file** in appropriate category folder
3. **Define patterns** with clear descriptions
4. **Test thoroughly** with various inputs
5. **Set appropriate severity** and action

**Example Custom Rule:**
```yaml
name: Custom Injection Pattern
details: Detects custom injection attempts
author: your name
severity: high
date: 2025-08-08
logsource:
    product: llm
    category: injection
    module: regex
patterns:
    language: llm-regex-pattern
    pattern: 
        - "(?i)(union|select|insert|delete|update|drop).*from"
        - "(?i)(exec|system|eval|shell_exec)"
references:
    - https://one_example
    - https://two_example
license: DRL 1.1
uuid: f1a2b3c4-d5e6-4f7a-8b8c-9d0e1f2a3b4c
action: block
```

#### Creating Custom Semgrep Rules

1. **Identify code vulnerability pattern**
2. **Write Semgrep pattern** using their syntax
3. **Test with sample code**
4. **Add appropriate metadata**
5. **Place in rules directory**

**Example Custom Semgrep Rule:**
```yaml
rules:
  - id: custom-sql-injection
    message: "Potential SQL injection vulnerability"
    languages: [python]
    severity: ERROR
    patterns:
      - pattern: |
          $QUERY = "SELECT * FROM $TABLE WHERE id = " + $USER_INPUT
    fix: |
      $QUERY = "SELECT * FROM $TABLE WHERE id = %s"
      # Use parameterized queries
```

## ⚙️ Enabling Disabled Pipeline

Some pipelines are disabled by default. To enable them:

### Enable OpenAI Pipeline
1. Configure your OpenAI API key in the .env configuration file:
   ```bash
   OPENAI_API_KEY=your-api-key
   OPENAI_MODEL=gpt-4
   ```

2. Add to your flow in `config.json`:
   ```json
   {
       "flow_name": "base",
       "pipelines": ["similarity", "regex", "openai"]
   }
   ```

### Enable ML Pipeline
1. Configure the model path in the .env configuration file:
   ```bash
   ML_MODEL_PATH=/path/to/your/model
   ```

2. Add to your flow in `config.json`:
   ```json
   {
       "flow_name": "base",
       "pipelines": ["similarity", "regex", "ml"]
   }
   ```

## 🔧 Adding Custom Pipelines

### Step 1: Create Pipeline Class

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

### Step 2: Register Pipeline

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

### Step 3: Add to Configuration

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

### Step 4: Add Pipeline Name to Enum

```python
# app/core/enums.py
class PipelineNames(str, Enum):
    # ... existing names
    my_pipeline = "my_pipeline"
```

## 🧪 Development

### Setting up OpenSearch

1. **Install OpenSearch**
   ```bash
   docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" opensearchproject/opensearch:latest
   ```

2. **Create similarity index**
   ```bash
   python app/pipelines/similarity_pipeline/index_script.py
   ```
   
   This will create the `similarity-prompt-index` index in OpenSearch. You can customize the index name by setting the SIMILARITY_PROMPT_INDEX environment variable.

### Setting up Kafka for Event Logging

AIDR Bastion supports Kafka integration for logging BLOCK and NOTIFY events, enabling scalable event streaming and real-time monitoring.

#### Quick Start with Docker Compose

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

#### Event Logging Features

- **BLOCK Events**: Logged when prompts are blocked by detection rules
- **NOTIFY Events**: Logged when prompts trigger notifications but are allowed
- **Structured JSON**: Events include prompt content, detection results, and metadata
- **Real-time Streaming**: Events are sent immediately to Kafka topics

#### Event Schema

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

#### Advanced Kafka Configuration

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

#### Rule Management
- **test_rules.py**: Comprehensive rule testing and validation
- **generate_rules.py**: Interactive rule creation and conversion
- **[Roota](https://github.com/UncoderIO/Roota)**: Public-domain language for collective cyber defense
- **[Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**: Convert Roota/Sigma rules to Semgrep format
- **[SOC Prime](https://socprime.com/)**: Access comprehensive threat detection rules

## 📄 License

This project is licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0) - see the [LICENSE](LICENSE) file for details.

For more information about LGPL, visit: https://www.gnu.org/licenses/lgpl-3.0.html

## 🛠️ Built With

This project is built using the following powerful open-source libraries and frameworks:

- **[Roota](https://github.com/UncoderIO/Roota)**: Public-domain language for collective cyber defense
- **[Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**: Convert Roota/Sigma rules to Semgrep format
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints
- **[OpenSearch](https://opensearch.org/)** - Open source search and analytics suite for log analytics, application search, and more
- **[OpenAI](https://openai.com/)** - AI research company providing powerful language models for intelligent content analysis
- **[Semgrep](https://semgrep.dev/)** - Static analysis tool for finding bugs and security issues in code
- **[Sentence Transformers](https://www.sbert.net/)** - Python framework for state-of-the-art sentence, text and image embeddings
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation and settings management using Python type annotations
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server implementation
- **[PyYAML](https://pyyaml.org/)** - YAML parser and emitter for Python
- **[NLTK](https://www.nltk.org/)** - Natural Language Toolkit for text processing


## 🛠️ TO-DO List

- Integrate API with SOC Prime for automatic rule synchronization and uploads
- Add local database storage for rules and events
- ✅ **Kafka support for scalable event streaming** - COMPLETED
- Develop an admin panel for managing events and detection rules
- Explore integration with [NOVA Rules](https://github.com/fr0gger/nova-framework/tree/main/nova_rules) to extend rule sources
- Add YARA-L support
>>>>>>> 289e2d8c5f586636389a0aaf51360c296f36602e
