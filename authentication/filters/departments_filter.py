import django_filters
from authentication import models


class DepartmentFilters(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(fields=(("name", "name"),))

    class Meta:
        model = models.Departement
        fields = (
            "name",
            "ordering",
        )
