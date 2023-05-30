from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def todo_form(request, todo_id=None):
    instance = None

    if todo_id:
        instance = Todo.objects.get(id=todo_id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()

            return HttpResponseRedirect(reverse("todo-form", kwargs={"todo_id": instance.id}))
    else:
        form = TodoForm(instance=instance)

    return render(request, "todo/todo_form.html", {"form": form})
