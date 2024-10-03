from dataclasses import dataclass, field

from .operation import Operation


@dataclass
class History:
    next_record: int | None = field(default=None)
    operations: list[Operation] = field(default_factory=list)
