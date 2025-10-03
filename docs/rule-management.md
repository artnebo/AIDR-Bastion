# Rule Management and Customization

## YAML Rules for Regex Pipeline

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

## Semgrep Rules for Code Analysis Pipeline

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

## Managing Rules

### Using Roota for Rule Creation

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

### Using Uncoder AI for Semgrep Rules

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

### Using SOC Prime for Advanced Rules

[SOC Prime](https://tdm.socprime.com/) provides comprehensive threat detection rules including Roota and Sigma formats:

1. **Visit [SOC Prime](https://tdm.socprime.com/)**
2. **Browse the Rules Library** (Sigma, Roota, and other formats)
3. **Filter by technology and threat type**
4. **Download or convert rules using [Uncoder AI](https://tdm.socprime.com/uncoder-ai/)**
5. **Adapt rules for your specific use case**

## Custom Rule Development

### Creating Custom Regex Rules

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

### Creating Custom Semgrep Rules

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
