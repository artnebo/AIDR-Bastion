# Pipelines

## 1. Regex Pipeline (`regex`)
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

## 2. Similarity Pipeline (`similarity`)
- **Purpose**: Vector-based similarity detection against known harmful prompts
- **Backend**: OpenSearch with vector search
- **Required**: OpenSearch configuration
- **Configuration**: `SIMILARITY_NOTIFY_THRESHOLD`, `SIMILARITY_BLOCK_THRESHOLD`
- **Best for**: Detecting variations of known attacks

## 3. Code Analysis Pipeline (`code_analysis`)
- **Purpose**: Static code analysis using Semgrep
- **Languages**: Python, JavaScript, Java, C++, and more
- **Rules**: Security-focused patterns
- **Best for**: Code injection and vulnerability detection

## 4. ML Pipeline (`ml`)
- **Purpose**: Machine learning-based classification
- **Configuration**: Requires `ML_PIPELINE_PATH`
- **Model**: Custom-trained model for prompt classification
- **Best for**: General malicious content detection
- **Required**: Configured environment `EMBEDDINGS_MODEL`

## 5. LLM Pipeline (`openai`)
- **Purpose**: AI-powered analysis using OpenAI GPT models
- **Configuration**: Requires `OPENAI_API_KEY` and `OPENAI_MODEL` (default is gpt-4). The `OPENAI_BASE_URL` environment variable is optional; by default, it is set to https://api.openai.com/v1
- **Features**: JSON response format, configurable models, intelligent decision-making
- **Response Format**: Returns structured JSON with status (block/notify/allow) and reasoning
- **Best for**: Complex reasoning and context-aware analysis
