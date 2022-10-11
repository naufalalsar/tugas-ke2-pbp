from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_finished =  models.BooleanField(default=False)


