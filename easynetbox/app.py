from .resource import Resource


class App:
    """
    Represents an app in the NetBox API, e.g. DCIM, IPAM.
    """
    def __init__(self, client, name):
        self._client = client
        self._name = name

    def resource(self, name):
        """
        Returns a resource object for the specified resource in the app.
        """
        return Resource(self._client, name, self._name)

    def __getattr__(self, name):
        # We support accessing resources as attributes
        return self.resource(name.replace("_", "-"))
