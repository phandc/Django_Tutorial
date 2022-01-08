from django import forms


from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # register Task as a model form
        fields = ["name", "complete"] #or fields = '__all__'

