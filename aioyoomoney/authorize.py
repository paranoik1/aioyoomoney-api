import requests

from urllib.parse import quote_plus
from yarl import URL

from .exceptions import EmptyToken
from .utils import raise_error


def authorize(client_id: str, redirect_uri: str, client_secret: str, scope: list[str]) -> str:
    redirect_uri = quote_plus(redirect_uri)
    url = (
        "https://yoomoney.ru/oauth/authorize?client_id={client_id}&response_type=code"
        "&redirect_uri={redirect_uri}&scope={scope}"
        .format(client_id=client_id, redirect_uri=redirect_uri, scope='%20'.join([str(elem) for elem in scope]))
    )

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        raise

    print("Visit this website and confirm the application authorization request:")
    print(response.url)

    code_or_url = URL(input("Enter redirected url (https://yourredirect_uri?code=XXXXXXXXXXXXX) or just code: "))
    code = code_or_url.query.get("code")
    if not code:
        code = code_or_url

    url = (
        "https://yoomoney.ru/oauth/token?code={code}&client_id={client_id}&"
        "grant_type=authorization_code&redirect_uri={redirect_uri}&client_secret={client_secret}"
        .format(code=code, client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret)
    )

    data = requests.post(url, headers=headers).json()
    if "error" in data:
        raise_error(data["error"])

    if data['access_token'] == "":
        raise EmptyToken()

    return data['access_token']
