from django.shortcuts import render
from .models import Todo
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def clear_message(request):
    return HttpResponse("")

def home(request):
    todos = Todo.objects.all().order_by("-id")
    context = {
        "todos": todos,
    }
    return render(request, "todo/home.html", context)


def create_todo(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    due_date = request.POST.get("due_date")
    todo = Todo.objects.create(title=title, description=description, due_date=due_date)
    # todo.save()

    todos = Todo.objects.all().order_by("-id")
    context = {
        "todos": todos,
    }
    return render(request, "todo/todo-list.html", context)


def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()

    todos = Todo.objects.all().order_by("-id")
    context = {
        "todos": todos,
    }
    return render(request, "todo/todo-list.html", context)


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by("-id")
    context = {
        "todos": todos,
    }
    return render(request, "todo/todo-list.html", context)


def todo_details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo": todo,
    }
    return render(request, "todo/todo_details.html")
