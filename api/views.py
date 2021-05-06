from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task, TaskGroup
from django.shortcuts import render
from .serializers import TaskSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Task List': '/task-list/',
        'Task Detail View': '/task-detail/<str:pk>/',
        'Task Create': '/task-create/',
        'Task Update': '/task-update/<str:pk>/',
        'Task Delete': '/task-delete/<str:pk>/',
        # 'Group List': '/group-list/',
        # 'Group Detail View': '/group-detail/<str:pk>/',
        # 'Group Create': '/group-create/',
        # 'Group Update': '/group-update/<str:pk>/',
        # 'Group Delete': '/group-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def group_detail(request, pk):
#     groups = TaskGroup.objects.get(id=pk)
#     serializer = TaskGroupSerializer(groups, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def group_list(request):
#     groups = TaskGroup.objects.filter(name=TaskGroup.name)
#     serializer = TaskGroupSerializer(groups, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def group_create(request):
#     serializer = TaskGroupSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save(user=request.user)

#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def group_update(request, pk):
#     group = TaskGroup.objects.get(id=pk)
#     serializer = TaskSerializer(instance=group, data=request.data)

#     user = request.user
#     if group.user != user:
#         return Response({'response': "You don't have permission to edit that."})

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# @permission_classes((IsAuthenticated,))
# def group_delete(request, pk):
#     group = TaskGroup.objects.get(id=pk)

#     user = request.user
#     if group.user != user:
#         return Response({'response': "You don't have permission to delete that."})
    
#     # check for active tasks using group and deny deletion

#     group.delete()

#     return Response('Group deleted!')

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    user = request.user
    if task.user != user:
        return Response({'response': "You don't have permission to edit that."})

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def task_delete(request, pk):
    task = Task.objects.get(id=pk)

    user = request.user
    if task.user != user:
        return Response({'response': "You don't have permission to delete that."})

    task.delete()

    return Response('Task deleted!')
