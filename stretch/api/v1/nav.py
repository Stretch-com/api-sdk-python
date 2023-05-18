from uuid import UUID

from stretch.client.base import Method

from .base import ApiBase, api_decoration_func, for_all_methods


@for_all_methods(api_decoration_func)
class Nav(ApiBase):
    """
    navigation Stretch API
    """

    def get_locations(self, **kwargs):
        """
        Get locations
        """
        return self._fetch(Method.get, "/nav/locations", json=kwargs)

    def post_location(self, **kwargs):
        """
        Create location
        """
        return self._fetch(Method.post, "/nav/location", json=kwargs)

    # def get_location(self, location_id: UUID, **kwargs):
    #    """
    #    Get service
    #    """
    #    return self._fetch(Method.get, f"/nav/location/{location_id}", json=kwargs)

    def put_location(self, location_id: UUID, **kwargs):
        """
        Update location
        """
        return self._fetch(Method.put, f"/nav/location/{location_id}", json=kwargs)

    def delete_location(self, location_id: UUID, **kwargs):
        """
        Delete service
        """
        return self._fetch(Method.delete, f"/nav/location/{location_id}", json=kwargs)
