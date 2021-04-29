from .models import Task, Sprint
from django_filters.rest_framework import (
    FilterSet, DateFilter
)
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskFilter(FilterSet):

    class Meta:
        model = Task
        fields = (
            'sprint', 'status',
            'assigned',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update(
            {'to_field_name': User.USERNAME_FIELD}
        )


class SprintFilter(FilterSet):

    # http://localhost:8000/api/sprints/?end_min=2021-07-9
    # will show all sprints that ended after 2021-07-9
    end_min = DateFilter(field_name='end', lookup_expr='gte')
    # http://localhost:8000/api/sprints/?end_min=2021-07-9
    # will show all sprints that ended before 2021-07-9
    end_max = DateFilter(field_name='end', lookup_expr='lte')

    class Meta:
        model = Sprint
        fields = ('end_min', 'end_max', )