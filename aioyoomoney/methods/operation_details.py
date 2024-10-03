from dateutil.parser import parse as dateutil_parse

from aioyoomoney.base.context_method import ContextMethod
from aioyoomoney.data_classes.operation import *
from aioyoomoney.enums.operation import OperationType
from aioyoomoney.utils import raise_error


OPERATIONS_TYPE = Operation | OperationDetails | OperationDetailsIncomingTransfer | OperationDetailsOutgoingTransfer | OperationDetailsPaymentShop


class OperationDetailsMethod(ContextMethod):
    def __init__(self, token: str, operation_id: str):
        super().__init__(
            token,
            "operation-details",
            "POST",
            data={
                "operation_id": operation_id
            }
        )

    async def __aenter__(self) -> OPERATIONS_TYPE:
        data = await super().__aenter__()

        if "error" in data:
            raise_error(data["error"])

        return self.get_operation_from_dict(data)

    @staticmethod
    def get_operation_from_dict(data: dict, details=True) -> OPERATIONS_TYPE:
        datetime = dateutil_parse(data.get("datetime", ""))

        data["datetime"] = datetime

        if not details:
            return Operation.serialize_from_dict(data)

        match data["type"]:
            case OperationType.PAYMENT_SHOP:
                if "digital_goods" in data:
                    articles = []
                    for product in data["digital_goods"]["article"]:
                        digital_article = DigitalArticle(merchant_article_id=product["merchantArticleId"],
                                                         serial=product["serial"],
                                                         secret=product["secret"])
                        articles.append(digital_article)

                    bonuses = []
                    for bonus in data["digital_goods"]["bonus"]:
                        digital_bonus = DigitalBonus(serial=bonus["serial"],
                                                     secret=bonus["secret"])
                        bonuses.append(digital_bonus)

                    data["digital_goods"] = DigitalGoods(articles=articles,
                                                         bonuses=bonuses)
                operation = OperationDetailsPaymentShop.serialize_from_dict(data)
            case OperationType.OUTGOING_TRANSFER:
                operation = OperationDetailsOutgoingTransfer.serialize_from_dict(data)
            case OperationType.INCOMING_TRANSFER:
                operation = OperationDetailsIncomingTransfer.serialize_from_dict(data)
            case _:
                operation = OperationDetails.serialize_from_dict(data)

        return operation
