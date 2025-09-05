from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    return render(request,"index.html")


def register(request):
    if register.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UserCreationForm()

    return render(request,'registration/register.html', {'form':form})






