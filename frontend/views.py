from api.models import TaskList
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render


@login_required(login_url='/login/')
def list(request) -> HttpResponse:
    lists = TaskList.objects.all().order_by("name")

    context = {
        "lists": lists,
    }

    return render(request, 'frontend/list.html', context)
