from api.models import Task, TaskGroup
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render


@login_required(login_url='/login/')
def list(request):

    return render(request, 'frontend/list.html')


def task_group(request) -> HttpResponse:
    groups = TaskGroup.objects.all().order_by("name")
    # Task.objects.filter(task_group)

    context = {
        "groups": groups
    }

    return render(request, "frontend/task_group.html", context)
