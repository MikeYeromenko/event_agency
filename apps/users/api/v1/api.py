from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from apps.events.filters import EventFilters
from apps.events.models import Event
from apps.users.api.v1.serializers import EventRetrieveSerializer, EventSerializer, EventUpdateSerializer


class EventV1API(BaseAPI):  # noqa  BaseAPI is a common custom class for APIs
    """
    Models description....
    """

    http_method_names = "get", "patch"
    queryset = Event.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = EventFilters

    class SerializerClasses:
        retrieve = EventRetrieveSerializer
        update = partial_update = EventUpdateSerializer
        default = EventSerializer

    class PermissionClasses:
        update = partial_update = (IsManager,)
