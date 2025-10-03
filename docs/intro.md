# Introduction

AIDR Bastion is a comprehensive GenAI protection system designed to safeguard against malicious prompts, injection attacks, and harmful content. The system incorporates multiple detection engines that operate sequentially to analyze and classify user inputs before reaching GenAI applications.

## Key Features

- **Multi-Pipeline Detection**: Regex patterns, ML models, vector-based similarity detection, and LLM-based analysis
- **Flexible Configuration**: Dynamic Pipeline configuration via JSON
- **Real-time Analysis**: Fast async processing with configurable thresholds
- **OpenSearch Integration**: Vector-based similarity search for prompt classification
- **RESTful API**: Easy integration with existing applications
- **Extensible Architecture**: Simple plugin system for custom Pipelines

## Supported Rule Sources

- The system supports [Roota](https://github.com/UncoderIO/Roota) and [Sigma rules](https://sigmahq.io/docs/guide/about.html), enabling the application of detection logic from multiple sources such as [SigmaHQ](https://github.com/SigmaHQ/sigma) (around 1,200 compatible free community Sigma rules available at release), [SOC Prime](https://tdm.socprime.com/) (with up to 3,000 additional compatible rules), and other third-party repositories.
- SOC Prime [Uncoder AI](https://tdm.socprime.com/uncoder-ai/) integration further extends functionality by translating Sigma rules into Semgrep format, providing standardized and reusable detection pipelines (requires a free account).
- Roota rules power the regex-based pipeline.
- The architecture supports rule extensibility, seamlessly integrating organization-specific signatures and external detection content.

## Additional Capabilities

- The system can also function as a local logging sensor, recording user and agent prompts and enabling diagnostics, incident discovery, and cyber attack investigation.
- Detection logic aligns with industry frameworks such as [MITRE ATLAS](https://atlas.mitre.org/) and [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/), ensuring standardized coverage against adversarial techniques.
- Actions include allow, block, or notify, depending on rule matches and policy configuration.

This layered detection approach delivers defense-in-depth against evolving adversarial prompt engineering and other AI-focused attack vectors.

Inspired by LlamaFirewall.

## Architecture

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
