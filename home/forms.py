from django import forms

from home.models import Task, DB

# forms.py
from django import forms
from home.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']



# forms.py

# forms.py

class DatabaseSelectionForm(forms.ModelForm):
    class Meta:
        model = DB
        fields = "__all__"

