from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def todo_form(request, todo_id=None):
    todo = None
    initial_data = {}

    if todo_id:
        todo = Todo.objects.get(id=todo_id)
        initial_data = {"title": todo.title, "description": todo.description}

    if request.method == "POST":
        form = TodoForm(request.POST, initial=initial_data)
        if form.is_valid():
            if todo_id:
                todo.title = form.cleaned_data["title"]
                todo.description = form.cleaned_data["description"]
                todo.save()
            else:
                todo = Todo(**form.cleaned_data)
                todo.save()
            return HttpResponseRedirect(f"{todo.id if todo.id else ''}")
    else:
        form = TodoForm(initial=initial_data)

    return render(request, "todo/todo_form.html", {"form": form})
