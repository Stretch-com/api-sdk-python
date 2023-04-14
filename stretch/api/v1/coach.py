import datetime
from uuid import UUID

from stretch.client.base import Method

from .base import ApiBase


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

    def get_availability(self, from_date: datetime.date = None, to_date: datetime.date = None):
        """
        Get availability list
        """
        params = {}
        if from_date is not None:
            params["from_date"] = from_date.strftime("%Y-%m-%d")
        if to_date is not None:
            params["to_date"] = to_date.strftime("%Y-%m-%d")

        return self._fetch(Method.get, "/coach/availability", params=params)

    def post_availability(self, **kwargs):
        """
        Create availability
        """
        return self._fetch(Method.post, "/coach/availability", json=kwargs)

    def put_availability(self, availability_id: UUID, **kwargs):
        """
        Update availability
        """
        return self._fetch(Method.put, f"/coach/availability/{availability_id}", json=kwargs)

    def delete_availability(self, availability_id: UUID, **kwargs):
        """
        Delete availability
        """
        return self._fetch(Method.delete, f"/coach/availability/{availability_id}", json=kwargs)

    def put_available(self, available: bool):
        """
        Update available state for self
        """
        return self._fetch(Method.put, f"/coach/available", json={"available": available})

    def get_calendar(self, from_date: datetime.date = None, to_date: datetime.date = None):
        """
        Get availability list
        """
        params = {}
        if from_date is not None:
            params["from_date"] = from_date.strftime("%Y-%m-%d")
        if to_date is not None:
            params["to_date"] = to_date.strftime("%Y-%m-%d")

        return self._fetch(Method.get, "/coach/availability/calendar", params=params)