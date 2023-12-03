from django.shortcuts import render, HttpResponse
from .models import Todo_Task

# Create your views here.
def sayHello(request):
    task_list = Todo_Task.objects.all()
    context = {"task_list": task_list}
    return render(request, "todo.html", context)
