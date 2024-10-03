from enum import StrEnum


class OperationStatus(StrEnum):
    SUCCESS = "success"
    REFUSED = "refused"
    IN_PROGRESS = "in_progress"


class OperationDirection(StrEnum):
    IN = "in"
    OUT = "out"


class OperationType(StrEnum):
    PAYMENT_SHOP = "payment-shop"
    OUTGOING_TRANSFER = "outgoing-transfer"
    DEPOSITION = "deposition"
    INCOMING_TRANSFER = "incoming-transfer"


class RecipientType(StrEnum):
    ACCOUNT = "account"
    PHONE = "phone"
    EMAIL = "email"
