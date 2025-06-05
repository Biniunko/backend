from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializers
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'tasks/home.html')
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        completed_status = request.query_params.get('completed', None)
        tasks = Task.objects.all()
        if completed_status is not None:
            tasks = tasks.filter(completed = completed_status.lower() == 'true')
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)