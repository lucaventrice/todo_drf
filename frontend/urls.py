from django.urls import path

from . import views


urlpatterns = [
    path('', views.list, name="list"),
    path('task_group/', views.task_group, name="task_group"),
]
