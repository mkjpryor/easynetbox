from easykube.rest import AsyncClient as BaseAsyncClient
from easykube.rest import SyncClient as BaseSyncClient

from .app import App
from .auth import TokenAuth


class SyncClient(BaseSyncClient):
    """
    Synchronous NetBox REST client.
    """

    def __init__(self, base_url, token, **kwargs):
        kwargs["base_url"] = base_url.rstrip("/").rstrip("/api") + "/api"
        kwargs["auth"] = TokenAuth(token)
        super().__init__(**kwargs)

    def app(self, name):
        """
        Get the app object with the given name.
        """
        return App(self, name)

    def __getattr__(self, name):
        # We support accessing apps as attributes
        return self.app(name)


class AsyncClient(BaseAsyncClient):
    """
    Asynchronous NetBox REST client.
    """

    def __init__(self, base_url, token, **kwargs):
        kwargs["base_url"] = base_url.rstrip("/").rstrip("/api") + "/api"
        kwargs["auth"] = TokenAuth(token)
        super().__init__(**kwargs)

    def app(self, name):
        """
        Get the app object with the given name.
        """
        return App(self, name)

    def __getattr__(self, name):
        # We support accessing apps as attributes
        return self.app(name.replace("_", "-"))
