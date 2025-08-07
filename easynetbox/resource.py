from easykube.rest import Resource as BaseResource


class Resource(BaseResource):
    """
    Represents a resource in the NetBox API, e.g. racks, devices.

    A resource belongs to an app.
    """

    def _prepare_path(self, id=None, params=None):  # noqa: A002
        # NetBox API URLs should always end in a /
        # IDs will likely be integers
        id = str(id) if id is not None else None  # noqa: A001
        path, params = super()._prepare_path(id, params)
        return path.rstrip("/") + "/", params

    def _extract_list(self, response):
        return response.json()["results"]

    def _extract_next_page(self, response):
        return response.json().get("next"), None
