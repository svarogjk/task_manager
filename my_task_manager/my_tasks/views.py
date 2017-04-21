from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    _tasks = Task.objects.all()
    return render(request, 'my_tasks/all_tasks.html',
                  {'tasks': _tasks})
