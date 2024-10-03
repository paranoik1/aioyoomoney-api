from datetime import datetime

from aioyoomoney.methods import *
from .data_classes import *
from .enums import *
from .methods.operation_details import OPERATIONS_TYPE


class Client:
    def __init__(self, token: str):
        self.token = token

    async def account_info(self) -> Account:
        async with AccountMethod(self.token) as account:
            return account

    async def operation_history(
            self,
            type: OperationHistoryType = None,
            label: str = None,
            from_date: datetime = None,
            till_date: datetime = None,
            start_record: str = None,
            records: int = None,
            details: bool = False
    ) -> History:
        async with HistoryMethod(
                token=self.token,
                type=type,
                label=label,
                from_date=from_date,
                till_date=till_date,
                start_record=start_record,
                records=records,
                details=details,
        ) as history:
            return history

    async def operation_details(self, operation_id: str) -> OPERATIONS_TYPE:
        async with OperationDetailsMethod(
                token=self.token,
                operation_id=operation_id,
        ) as operation_details:
            return operation_details

