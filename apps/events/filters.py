from django_filters import CharFilter, FilterSet

from apps.events.models import Event


class EventFilters(FilterSet):
    title = CharFilter(field_name="search_field", lookup_expr="icontains")

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        # logic
        return queryset

    class Meta:
        model = Event
        fields = {...}
