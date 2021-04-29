from .models import Task
from django_filters.rest_framework import (
    FilterSet,
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