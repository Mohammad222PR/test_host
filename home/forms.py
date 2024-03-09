from django import forms

from home.models import Task, DB

# forms.py
from django import forms
from home.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    def save(self, commit=True, using=None):
        instance = super(TaskForm, self).save(commit=False)
        instance.save(using=using)
        return instance

# forms.py

# forms.py

class DatabaseSelectionForm(forms.ModelForm):
    class Meta:
        model = DB
        fields = "__all__"

