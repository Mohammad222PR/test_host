from django.db import models
from django.http import JsonResponse
from django.db import connection
from django.conf import settings


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


