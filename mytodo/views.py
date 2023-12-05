from django.shortcuts import render, HttpResponse
from .models import Todo_Task
from .forms import TodoForm

# Create your views here.
def displayToDo(request):
    task_list = Todo_Task.objects.all()
    form = TodoForm()
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TodoForm(request.POST)
            else:
                task = Todo_Task.objects.get(id=pk)
                form = TodoForm(request.POST, instance=task)
            form.save()
            form = TodoForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            task = Todo_Task.objects.get(id=pk)
            task.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            task = Todo_Task.objects.get(id=pk)
            form = TodoForm(instance=task)
    context = {
        "task_list": task_list,
        "form": form
        }
    return render(request, "todo.html", context)
