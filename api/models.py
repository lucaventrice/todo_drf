from django.conf import settings
from django.db import models


class TaskGroup(models.Model):
    name = models.CharField(max_length=60, unique=True)
    tasks = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    task_group = models.OneToOneField(TaskGroup, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
