import django_filters
from .models import Todo


class TodoFilter(django_filters.FilterSet):
    created_gte = django_filters.DateFilter(field_name="created", lookup_expr="gte", label="Created After")
    created_lte = django_filters.DateFilter(field_name="created", lookup_expr="lte", label="Created Before")

    class Meta:
        model = Todo
        fields = [
            "todo_status",
            "created_gte",
            "created_lte",
        ]