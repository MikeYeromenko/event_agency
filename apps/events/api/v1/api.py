from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from apps.events.models import Event
from apps.users.api.v1.serializers import EventRetrieveSerializer, EventSerializer, EventUpdateSerializer


class EventV1API(BaseAPI):  # noqa  BaseAPI is a common custom class for APIs
    """
    Models description....
    """

    http_method_names = "get", "patch", "post", "delete"
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

    def get_queryset(self):
        return Event.objects.select_related("organizer")

    @swagger_auto_schema(responses={200: EventSerializer})
    @action(
        detail=False,
        methods=("post",),
        name="Register event",
        url_path="register",
        serializer_class=EventSerializer,
        permission_classes=(IsManager,),
    )
    def register_event(self, *_args, **_kwargs):
        ...
        serializer.register_event(...)
        return Response(response_serializer.data)
