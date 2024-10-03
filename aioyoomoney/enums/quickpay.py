from enum import StrEnum


class PaymentType(StrEnum):
    # оплата из кошелька ЮMoney;
    PC = "PC"
    # оплата с банковской карты.
    AC = "AC"
