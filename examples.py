import asyncio

from dataclasses import fields
from aioyoomoney import *


def get_token(client_id: str, redirect_uri: str, client_secret: str):
    token = authorize(
        client_id=client_id,
        redirect_uri=redirect_uri,
        client_secret=client_secret,
        scope=[
            "account-info",
            "operation-history",
            "operation-details",
            "incoming-transfers",
            "payment-p2p",
        ]
    )

    print(token)
    return token


async def get_operation_history(token: str):
    client = Client(token)

    history = await client.operation_history()
    print("Next record:", history.next_record)
    for operation in history.operations:
        for field in fields(operation):
            if field.name != "kwargs":
                print(field.name, '->', operation[field.name])

        for key, value in operation.kwargs.items():
            print(key, '->', value)

        print("================================")


async def get_operation_details(token: str):
    client = Client(token)
    history = await client.operation_history()

    for operation in history.operations:
        operation = await client.operation_details(operation.operation_id)
        for field in fields(operation):
            if field.name != "kwargs":
                print(field.name, '->', operation[field.name])

        for key, value in operation.kwargs.items():
            print(key, '->', value)

        print("================================")



async def client_info(token: str):
    client = Client(token)

    account = await client.account_info()
    print(f"Account: {account.id}")
    print(f"Balance: {account.balance}")
    print(f"Currency: {account.currency}")
    print(f"Account Status: {account.account_status}")
    print(f"Account Type: {account.account_type}")
    print(f"Balance Details: {account.balance_details}")
    print(f"Cards Linked: {account.cards_linked}")



async def quickpay(receiver: str, sum: int, label: str = None):
    async with Quickpay(
        receiver=receiver,
        sum=sum,
        label=label
    ) as quickpay:
        print(quickpay.url)


# asyncio.run(quickpay())
