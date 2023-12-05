from django import forms
from .models import Todo_Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = ['task']