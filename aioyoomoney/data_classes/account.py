from dataclasses import dataclass, field

from .balance_details import BalanceDetails
from .card import Card
from ..enums.account import *


@dataclass
class Account:
    id: str = field(default="")
    balance: float = field(default=0.0)
    account_type: AccountType | None = field(default=None)
    account_status: AccountStatus | None = field(default=None)
    balance_details: BalanceDetails | None = field(default=None)
    cards_linked: list[Card] = field(default_factory=list)
    currency: int = field(default=643)
    identified: bool = field(default=False)
