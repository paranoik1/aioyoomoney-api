# 🚀 Yoomoney API (async) - Неофициальная Python библиотека

<div style="text-align: center">
    
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Version](https://img.shields.io/pypi/v/aioyoomoney-api)

> Асинхронная Python библиотека для работы с API [YooMoney](https://yoomoney.ru).

</div>

🔗 **Основано на репозитории**: [AlekseyKorshuk/yoomoney-api](https://github.com/AlekseyKorshuk/yoomoney-api)

## 📖 Введение

Библиотека разработана на основе официальной документации [YooMoney](https://yoomoney.ru/docs/wallet).

## 🌟 Возможности

Реализованные методы:

- [Получение токена доступа](#access-token) для доступа к API сервису
- [Информация об аккаунте](#client-info) - Получение информации о статусе пользовательского аккаунта
- [История операций](#operation-history) - Просмотр полной или частичной истории операций с постраничной навигацией
- [Детали операции](#operation-details) - Подробная информация о конкретной операции
- [Формы быстрой оплаты](#quickpay-forms) - Встраиваемые платежные формы для перевода средств

## 📦 Установка

Установка через pip:

```bash
pip install aioyoomoney-api
```

Установка из исходников:

```bash
git clone https://github.com/paranoik1/aioyoomoney-api
cd aioyoomoney-api
pip install .
```

## 🚀 Быстрый старт

### <a name="access-token"></a>🔑 Получение токена доступа

1. Войдите в свой [YooMoney кошелек](https://yoomoney.ru). Если у вас его нет - [создайте](https://yoomoney.ru/reg)
2. Перейдите на страницу [регистрации приложения](https://yoomoney.ru/myservices/new)
3. Заполните параметры приложения. Сохраните CLIENT_ID и REDIRECT_URI
4. Нажмите кнопку "Подтвердить"
5. Замените YOUR_CLIENT_ID, YOUR_REDIRECT_URI и YOUR_CLIENT_SECRET на реальные значения

```python
from aioyoomoney import authorize

token = authorize(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    client_secret=CLIENT_SECRET,
    scope=[
        "account-info",
        "operation-history",
        "operation-details",
        "incoming-transfers",
        "payment-p2p",
    ]
)

print(token)
```

### <a name="client-info"></a>💳 Информация об аккаунте

```python
import asyncio
from aioyoomoney import Client

async def client_info():
    client = Client(YOUR_TOKEN)
    account = await client.account_info()

    print(f"Аккаунт: {account.id}")
    print(f"Баланс: {account.balance}")
    print(f"Валюта: {account.currency}")
    print(f"Статус: {account.account_status}")
    print(f"Тип аккаунта: {account.account_type}")
    print(f"Детали баланса: {account.balance_details}")
    print(f"Привязанные карты: {account.cards_linked}")

asyncio.run(client_info())
```

### <a name="operation-history"></a>📜 История операций

```python
import asyncio
from aioyoomoney import Client
from dataclasses import fields

async def get_operation_history():
    client = Client(YOUR_TOKEN)
    history = await client.operation_history()
    
    print("Следующая запись:", history.next_record)
    for operation in history.operations:
        for field in fields(operation):
            if field.name != "kwargs":
                print(f"{field.name} -> {operation[field.name]}")

        for key, value in operation.kwargs.items():
            print(f"{key} -> {value}")

        print("="*30)

asyncio.run(get_operation_history())
```

### <a name="operation-details"></a>🔍 Детали операции

```python
import asyncio
from aioyoomoney import Client
from dataclasses import fields

async def get_operation_details():
    client = Client(YOUR_TOKEN)
    operation = await client.operation_details(OPERATION_ID)
    
    for field in fields(operation):
        if field.name != "kwargs":
            print(f"{field.name} -> {operation[field.name]}")

    for key, value in operation.kwargs.items():
        print(f"{key} -> {value}")

asyncio.run(get_operation_details())
```

### <a name="quickpay-forms"></a>💸 Формы быстрой оплаты

```python
import asyncio
from aioyoomoney import Quickpay

async def quickpay():
    async with Quickpay(
        receiver="4100111111111111",
        quickpay_form="shop",
        targets="Поддержка проекта",
        payment_type="SB",
        sum=10,
        form_comment='Тестовая оплата',
        label="order123"
    ) as quickpay:
        print(f"URL: {quickpay.redirected_url}")
        print(f"Базовый URL с параметрами: {quickpay.base_url}")
        print(f"Параметры: {quickpay.payload}")

asyncio.run(quickpay())
```
