import aiohttp

from .base import ContextSession
from .enums.quickpay import PaymentType


QUICKPAY_URL = "https://yoomoney.ru/quickpay/confirm"


# https://yoomoney.ru/docs/payment-buttons/using-api/forms
class Quickpay(ContextSession):
    def __init__(
            self,
            receiver: str,
            sum: float,
            payment_type: PaymentType = None,
            label: str = None,
            success_url: str = None,
    ):
        self.data = {
            "receiver": receiver,
            "quickpay-form": "button",
            "paymentType": payment_type,
            "sum": sum,
            "label": label,
            "successURL": success_url,
        }

        self.data = {k: v for k, v in self.data.items() if v is not None}

        self.url = None

        super().__init__(QUICKPAY_URL, "POST", data=self.data)

    async def __aenter__(self) -> "Quickpay":
        response = await super().__aenter__()
        self.url = response.url

        return self
