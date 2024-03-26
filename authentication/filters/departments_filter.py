from authentication import models

import django_filters


class DepartmentFilters(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(fields=("name",))

    class Meta:
        model = models.Departement
        fields = (
            "name",
            "ordering",
        )
