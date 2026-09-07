from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages

def home(request):

    if request.method == "POST":

        date = request.POST.get("date")
        time = request.POST.get("time")
        text = request.POST.get("text")

        Task.objects.create(date=date, time=time, text=text)
        messages.success(request,"Task Added Successfully.s")

        return redirect('home')
    

    tasks = Task.objects.all().order_by("date","time")
    return render(request, "home.html", {"tasks" :tasks})

# view tasks
def task_list(request):
    tasks = Task.objects.all().order_by("date", "time")

    return render(request, "task_list.html", {"tasks": tasks})


#edit task

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.date = request.POST.get("date")
        task.time = request.POST.get("time")
        task.text = request.POST.get("text")

        task.save()

        return redirect("task_list")

    return render(request, "edit_task.html", {"task": task})

def delete_list_item(request, id):
    task = get_object_or_404(Task , id=id)

    task.delete()
    return redirect("task_list")