from django.shortcuts import render, redirect
from django.views import View

from home.forms import TaskForm
from home.models import Task


# Create your views here.


def home(request):
    if request.method == 'GET':
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'home/index.html', {'tasks': tasks, 'form': form})

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'home/index.html')
