from django.shortcuts import render
from django.views.generic import ListView
from todo.models import ToDoItem
from datetime import date

class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

class TodayToDos(ListView):
    model = ToDoItem
    template_name = "todo/today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())



