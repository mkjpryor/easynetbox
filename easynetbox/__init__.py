"""EasyNetBox - A simple client for NetBox supporting sync and async access patterns."""

from .auth import TokenAuth
from .client import AsyncClient, SyncClient
from .resource import Resource

__version__ = "0.1.0"
__all__ = ["AsyncClient", "Resource", "SyncClient", "TokenAuth"]
