from django.urls import path

# from .views import todo_create
from . import views

urlpatterns = [
    path("", views.todo_form),
    path("<int:todo_id>", views.todo_form),
]
