from django.conf.urls import url
from . import views

urlpatterns = [
    #all tasks
    url(r'^$', views.task_list, name='task_list'),
]