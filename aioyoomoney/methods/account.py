from ..base.context_method import ContextMethod
from ..data_classes import *


class AccountMethod(ContextMethod):
    def __init__(self, token: str):
        super().__init__(token, "account-info")

    async def __aenter__(self) -> Account:
        data = await super().__aenter__()

        return self._get_account_object(data)

    def _get_account_object(self, data: dict) -> Account:
        account = Account()
        account.id = data['account']
        account.balance = data['balance']
        account.currency = data['currency']
        account.account_status = data['account_status']
        account.account_type = data['account_type']
        account.identified = data["identified"]

        if 'balance_details' in data:
            balance_details = data['balance_details']
            account.balance_details = BalanceDetails()
            account.balance_details.available = float(balance_details.get('available', 0.0))
            account.balance_details.blocked = float(balance_details.get('blocked', 0.0))
            account.balance_details.debt = float(balance_details.get('debt', 0.0))
            account.balance_details.deposition_pending = float(balance_details.get('deposition_pending', 0.0))
            account.balance_details.total = float(balance_details.get('total', 0.0))
            account.balance_details.hold = float(balance_details.get('hold', 0.0))

        if 'cards_linked' in data:
            for card_linked in data['cards_linked']:
                card = Card(
                    pan_fragment=card_linked['pan_fragment'],
                    type=card_linked['type']
                )
                account.cards_linked.append(card)

        return account
