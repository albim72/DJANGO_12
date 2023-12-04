from django.shortcuts import render
from django.views.generic import ListView
from todo.models import ToDoItem

class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"


