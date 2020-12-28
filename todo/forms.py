from django import forms
from django.forms import ModelForm

from todo.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'
