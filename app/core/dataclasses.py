from dataclasses import dataclass

from app.core.enums import RuleAction


@dataclass
class Rule:
    id: str
    name: str
    details: str
    language: str
    body: str
    action: RuleAction


@dataclass
class SemgrepLangConfig:
    file_extension: str
    config_name: str | None = None
