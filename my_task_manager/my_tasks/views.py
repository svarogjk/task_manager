from django.shortcuts import render, get_object_or_404
from .models import Task
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from common.decorators import ajax_required

# Create your views here.


class TaskListView(ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'my_tasks/all_tasks.html'


@csrf_protect
@ajax_required
@require_POST
def task_add(request):
    _task_description = request.POST.get('task_description')

    task = Task(task_description=_task_description)
    task.save()

    return JsonResponse({'task_id': task.task_id})


@csrf_protect
@ajax_required
@require_POST
def task_delete(request):
    # task_text
    _task_id = request.POST.get('task_id')

    required_task = Task.objects.get(task_id=_task_id)
    required_task.delete()

    return JsonResponse({'status': 'OK'})


@csrf_protect
@ajax_required
@require_POST
def task_edit(request):
    _task_id = request.POST.get('task_id')
    _task_description = request.POST.get('task_description')

    required_task = Task.objects.get(task_id=_task_id)
    required_task.task_description = _task_description
    required_task.save()

    return JsonResponse({'status': 'OK'})




