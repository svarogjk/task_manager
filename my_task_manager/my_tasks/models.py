from django.db.models import (Model, AutoField, TextField)

# Create your models here.

class Task(Model):
    task_id = AutoField(primary_key=True)
    task_description = TextField(max_length=1000)

    def __str__(self):
        return self.task_id
