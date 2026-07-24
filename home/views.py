from django.shortcuts import render,redirect
from .models import ToDo
from django.contrib import messages
from .forms import TodoCreateForm,UpdateForm

def homepage(request):
    todo = ToDo.objects.all()
    return render(request,"home.html",{"todo":todo})


def details(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    return render(request, 'detail.html',{'todo':todo})


def delete(request,todo_id):
    ToDo.objects.get(id=todo_id).delete()
    messages.success(request,"this is test","success")
    return redirect('home')


def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ToDo.objects.create(title=cd['title'],body=cd['body'],create=cd['create'])
            messages.success(request,"create item successfully","success")
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request,"create.html",{"form":form})


def update(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == "POST":
        form = UpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,"update item successfully","success")
            return redirect('details',todo_id)
    else:
        form = UpdateForm(instance=todo)
    return render(request,"update.html",{"form":form})

