from django.db import models
from django.conf import settings


class Sprint(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or f'Sprint ending {self.end}'


class Task(models.Model):
    """Unit of work to be done for the sprint."""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4
    STATUS_CHOICES = (
        (STATUS_TODO, 'Not Started'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_TESTING, 'Testing'),
        (STATUS_DONE, 'Done'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        blank=True, on_delete=models.CASCADE
    )
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name