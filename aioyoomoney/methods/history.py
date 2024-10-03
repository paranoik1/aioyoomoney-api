from datetime import datetime
from pprint import pprint

from .operation_details import OperationDetailsMethod
from ..base.context_method import ContextMethod
from ..data_classes import *
from ..enums.history import OperationHistoryType
from ..exceptions import (
    IllegalParamFromDate,
    IllegalParamTillDate,
)
from ..utils import raise_error, convert_datetime_to_str


class HistoryMethod(ContextMethod):
    def __init__(
            self, token: str = None,
            type: OperationHistoryType = None,
            label: str = None,
            from_date: datetime = None,
            till_date: datetime = None,
            start_record: str = None,
            records: int = None,
            details: bool = False
    ):
        self.details = details

        try:
            from_date = convert_datetime_to_str(from_date)
        except:
            raise IllegalParamFromDate()

        try:
            till_date = convert_datetime_to_str(till_date)
        except:
            raise IllegalParamTillDate()

        payload = {
            "type": type,
            "label": label,
            "from": from_date,
            "till": till_date,
            "start_record": start_record,
            "records": records,
            "details": str(details).lower()
        }

        payload = {k: v for k, v in payload.items() if v is not None}
        super().__init__(token, "operation-history", data=payload)

    async def __aenter__(self) -> History:
        data = await super().__aenter__()

        if "error" in data:
            raise_error(data["error"])

        history = History()

        if "next_record" in data:
            history.next_record = int(data["next_record"])

        for operation_data in data["operations"]:
            operation = OperationDetailsMethod.get_operation_from_dict(operation_data, self.details)

            history.operations.append(operation)

        return history
