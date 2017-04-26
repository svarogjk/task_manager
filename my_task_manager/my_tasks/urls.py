from django.conf.urls import url
from . import views

urlpatterns = [
    #all tasks
    url(r'^$', views.TaskListView.as_view(), name='task_list'),
    url(r'^add/$', views.task_add, name='task_add'),
    url(r'^edit/$', views.task_edit, name='task_edit'),
    url(r'^delete/$', views.task_delete, name='task_delete'),
]