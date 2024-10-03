from enum import StrEnum


class AccountStatus(StrEnum):
    ANONYMOUS = "anonymous"
    NAMED = "named"
    IDENTIFIED = "identified"


class AccountType(StrEnum):
    PROFESSIONAL = "professional"
    PERSONAL = "personal"
