from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import tasks

from tasks.models import Task
from .forms import TaskForm

# Create your views here.

def index(request):

    tasks = Task.objects.all()
    form = TaskForm() #if method is get then returning the empty form

    if request.method == 'POST':
        print("request: ", request)
        print("post request", request.POST) #request.POST is a dictionary that contains form fields and their attributes.
        #create a form instance and populat it with data from the request
         
        form = TaskForm(request.POST)

        if form.is_valid():
             #save data
             form.save()
             return redirect('/')
         
    

    context = {'tasks': tasks, 'form': form}

    return render(request, "tasks/index.html", context)  #HttpResponse("") not string


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task) #if method is get then returning the form values.

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update.html', context)

def delete(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)