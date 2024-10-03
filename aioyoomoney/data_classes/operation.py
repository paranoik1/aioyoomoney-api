from dataclasses import field, fields
from datetime import datetime as dt

from aioyoomoney.data_classes.digital import *
from aioyoomoney.enums.operation import *


@dataclass
class Operation:
    operation_id: str | None = field(default=None)
    status: OperationStatus | None = field(default=None)
    datetime: dt | None = field(default=None)
    title: str | None = field(default=None)
    pattern_id: str | None = field(default=None)
    direction: OperationDirection | None = field(default=None)
    amount: float | None = field(default=None)
    label: str | None = field(default=None)
    type: OperationType | None = field(default=None)
    kwargs: dict = field(default_factory=dict)

    @classmethod
    def serialize_from_dict(cls, data: dict) -> "Operation":
        operation = cls()

        valid_keys = [_field.name for _field in fields(operation)]  # не нравится
        for key, value in data.items():
            if key in valid_keys:
                operation.__setattr__(key, value)
            else:
                operation.kwargs[key] = value

        return operation

    def __getitem__(self, item: str):
        if item in self.kwargs.keys():
            return self.kwargs.get(item)

        return self.__getattribute__(item)


@dataclass
class OperationDetails(Operation):
    details: str | None = field(default=None)
    codepro: bool | None = field(default=None)
    comment: str | None = field(default=None)
    message: str | None = field(default=None)


@dataclass
class OperationDetailsIncomingTransfer(OperationDetails):
    sender: str | None = field(default=None)

    def __post_init__(self):
        self.type = OperationType.INCOMING_TRANSFER


@dataclass
class OperationDetailsOutgoingTransfer(OperationDetails):
    recipient: str | None = field(default=None)
    recipient_type: RecipientType | None = field(default=None)
    amount_due: int | None = field(default=None)
    fee: int | None = field(default=None)

    def __post_init__(self):
        self.type = OperationType.OUTGOING_TRANSFER


@dataclass
class OperationDetailsPaymentShop(OperationDetailsOutgoingTransfer):
    digital_goods: DigitalGoods | None = field(default=None)

    def __post_init__(self):
        self.type = OperationType.PAYMENT_SHOP
