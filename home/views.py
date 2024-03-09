import os

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core.settings import BASE_DIR
from home.forms import TaskForm
from home.models import Task
from .forms import DatabaseSelectionForm
from django.db import connections


# Create your views here.


def home(request):

    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, "home/index.html", {"tasks": tasks})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/")

    return render(request, "home/index.html", {"form": form})


def delete_task(request, pk):
    if request.method == "GET":
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('/')

    return render(request, 'home/index.html')


# views.py
# views.py


@csrf_exempt
def connect_to_database(request):
    if request.method == 'POST':
        if request.POST.get('mysql'):
            # انجام عملیات برای MYSQL_DB=True
            os.remove(BASE_DIR / ".env")
            file = open(".env", "wb")
            file.write(b'MYSQL_DB=True')
            file.close()

        elif request.POST.get('sql'):
            os.remove(BASE_DIR / ".env")
            file = open(".env", "wb")
            file.write(b'MYSQL_DB=False')
            file.close()
        return redirect('/')

    return render(request, 'your_template.html')