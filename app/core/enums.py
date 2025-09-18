from enum import Enum


class PipelineNames(str, Enum):
    openai = "openai"
    ml = "ml"
    code_analysis = "code_analysis"
    personal_info = "personal_info"
    regex = "regex"
    similarity = "similarity"


class ActionStatus(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    NOTIFY = "notify"


class PipelineLabel(str, Enum):
    CLEAR = "clear"


class Language(str, Enum):
    C = "c"
    CPP = "cpp"
    CSHARP = "csharp"
    GOLANG = "golang"
    HACK = "hack"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    KOTLIN = "kotlin"
    PHP = "php"
    PYTHON = "python"
    RUBY = "ruby"
    RUST = "rust"
    SWIFT = "swift"
    LANGUAGE_AGNOSTIC = "language_agnostic"

    def __str__(self) -> str:
        return self.name.lower()


class RuleAction(str, Enum):
    NOTIFY = "notify"
    BLOCK = "block"
