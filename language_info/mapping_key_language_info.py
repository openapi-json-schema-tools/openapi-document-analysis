import dataclasses
import typing

@dataclasses.dataclass
class MappingKeyLanguagInfo:
    unique_keys: int
    case_insensitieve_collisions: typing.Dict[str, str] = dataclasses.field(default_factory=lambda: {})
    invalid_identifiers: typing.Dict[str, str] = dataclasses.field(default_factory=lambda: {})
