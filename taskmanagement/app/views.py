from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_user=request.user)
    return render(request, 'task_detail.html', {'task': task})
