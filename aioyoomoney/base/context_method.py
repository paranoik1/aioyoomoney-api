from os.path import join

from .context_session import ContextSession
from ..exceptions import InvalidToken
from ..globals import API_URL


class ContextMethod(ContextSession):
    def __init__(self, token: str, method: str, http_method: str = "POST", **kwargs):
        self.token = token
        self.headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        super().__init__(
            url=join(API_URL, method),
            method=http_method,
            headers=self.headers,
            **kwargs
        )

    async def __aenter__(self) -> dict:
        response = await super().__aenter__()
        response_json = await response.json()

        if not response_json:
            raise InvalidToken()

        return response_json
