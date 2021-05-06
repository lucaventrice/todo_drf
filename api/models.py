from django.conf import settings
from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Task Lists"


class Task(models.Model):
    title = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
