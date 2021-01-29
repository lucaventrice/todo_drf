from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def list(request):
    return render(request, 'frontend/list.html')
