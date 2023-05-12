from uuid import UUID

from stretch.client.base import Method

from .base import ApiBase, api_decoration_func, for_all_methods


@for_all_methods(api_decoration_func)
class Coach(ApiBase):
    """
    Coach Stretch API
    """

    def get_servicetypes(self, **kwargs):
        """
        Get service types information
        """
        return self._fetch(Method.get, "/servicetypes", json=kwargs)

    def get_services(self, **kwargs):
        """
        Get services information
        """
        return self._fetch(Method.get, "/coach/services", json=kwargs)

    def post_service(self, **kwargs):
        """
        Create service
        """
        return self._fetch(Method.post, "/coach/service", json=kwargs)

    def get_service(self, service_id: UUID, **kwargs):
        """
        Get service
        """
        return self._fetch(Method.get, f"/coach/service/{service_id}", json=kwargs)

    def put_service(self, service_id: UUID, **kwargs):
        """
        Update service
        """
        return self._fetch(Method.put, f"/coach/service/{service_id}", json=kwargs)

    def delete_service(self, service_id: UUID, **kwargs):
        """
        Delete service
        """
        return self._fetch(Method.delete, f"/coach/service/{service_id}", json=kwargs)

    def get_coach_profile(self, coach_id: UUID, **kwargs):
        """
        Get coach profile
        """
        return self._fetch(Method.get, f"/coach/{coach_id}/profile", json=kwargs)
