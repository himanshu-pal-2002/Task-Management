from django.db import models
from django.contrib.auth.models import User


# Models for Task:
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, default='To Do')
    priority = models.CharField(max_length=20, default='Medium')
    due_date = models.DateField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
