import os

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core.settings import BASE_DIR
from home.forms import TaskForm
from home.models import Task
from .forms import DatabaseSelectionForm
from django.db import connections
import subprocess

# Create your views here.

db = settings.MYSQL_DB


def home(request):
    if request.method == "GET":
        if db:
            tasks = Task.objects.using('default').all()
        elif db == False:
            tasks = Task.objects.using('default').all()
        return render(request, "home/index.html", {"tasks": tasks})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            if db:
                form.save(using='default')
            if db == False:
                form.save(using='default')
            return redirect("/")

    return render(request, "home/index.html", {"form": form})


def delete_task(request, pk):
    if request.method == "GET":
        if db:
            task = Task.objects.using("default").get(id=pk)
            task.delete()
        if db == False:
            task = Task.objects.using("default").get(id=pk)
            task.delete()
        return redirect('/')

    return render(request, 'home/index.html')


# views.py
# views.py


@csrf_exempt
def connect_to_database(request):
    if request.method == 'POST':
        if request.POST.get('mysql'):
            os.remove(BASE_DIR / ".env")
            file = open(".env", "wb")
            file.write(b'MYSQL_DB=True')
            file.close()

        elif request.POST.get('sql'):
            os.remove(BASE_DIR / ".env")
            file = open(".env", "wb")
            file.write(b'MYSQL_DB=False')
            file.close()

        subprocess.run(["python", "manage.py", "runserver"])
        return redirect('/')

    return render(request, 'home/selectdb.html')
