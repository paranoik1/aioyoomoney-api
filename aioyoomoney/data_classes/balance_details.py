from dataclasses import dataclass, field


@dataclass
class BalanceDetails:
    total: float | None = field(default=None)
    available: float | None = field(default=None)
    deposition_pending: float | None = field(default=None)
    blocked: float | None = field(default=None)
    debt: float | None = field(default=None)
    hold: float | None = field(default=None)
