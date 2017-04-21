from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'task_description']
    ordering = ['task_id']


# Register your models here.
admin.site.register(Task, TaskAdmin)