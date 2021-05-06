from django.urls import path

from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('group-list/', views.group_list, name='group-list'),
    path('task-detail/<str:pk>/', views.task_detail, name='task-detail'),
    path('group-detail/<str:pk>/', views.group_detail, name='group-detail'),
    path('group-create/', views.group_create, name='group-create'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<str:pk>/', views.task_update, name='task-update'),
    path('group-update/<str:pk>/', views.group_update, name='group-update'),
    path('task-delete/<str:pk>/', views.task_delete, name='task-delete'),
    path('group-delete/<str:pk>/', views.group_delete, name='group-delete'),
]
