from aiohttp import ClientSession, ClientResponse
from yarl import URL


class ContextSession:
    def __init__(self, url: str | URL, method: str, **kwargs):
        self._session = None
        self._response = None

        self.__url = url
        self.__method = method
        self.__kwargs = kwargs

    async def __aenter__(self) -> ClientResponse:
        self._session = ClientSession()
        self._response = await self._session.request(
            self.__method,
            self.__url,
            **self.__kwargs
        )

        return self._response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._response.close()
        await self._session.close()
