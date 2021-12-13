from django.forms.widgets import RadioSelect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .form import CreateNewList

# Create your views here.
#1.create a Django project
#django-admin startproject mysite

#2.run server
#python manage.py runserver

#3.Create a main app. An app is a web application that does something.
#python manage.py startapp main

#migrate all data changes]
#python manage.py migrate

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == 'POST':
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked": #get a item and its value in dict
                        item.complete =True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls":ls})
        
    return render(response, "main/home.html", {})

def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] #get the data cryted
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            # t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})