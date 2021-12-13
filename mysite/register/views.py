from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            print("Saved user")
        return redirect('/')
    else:
        form =  RegisterForm()
        print("Blannk")

    return render(response, "register/register.html", {"form":form})