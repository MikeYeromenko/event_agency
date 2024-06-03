from rest_framework import serializers

from apps.events.models import Event
from integrations.emails.client import emails_client


class EventSerializer(serializers.ModelSerializer):
    """
    ...
    """

    class Meta:
        model = Event
        fields = "__all__"

    def register_event(self):
        # logic
        send_email_task.delay()
        ...


class EventRetrieveSerializer(serializers.ModelSerializer):
    """
    ...
    """

    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"


class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (...,)
        extra_kwargs = {field: {"required": False} for field in fields}
