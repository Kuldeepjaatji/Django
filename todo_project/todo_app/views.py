from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'todo_app/task_list.html', {'tasks': tasks, 'form': form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
