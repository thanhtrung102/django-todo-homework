from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# 1. List all Todos
def todo_list(request):
    todos = Todo.objects.all().order_by('due_date')
    return render(request, 'todo_list.html', {'todos': todos})

# 2. Create a Todo
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todo_list')
    return render(request, 'todo_create.html')

# 3. Delete a Todo
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')

# 4. Mark as Resolved
def todo_toggle_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    return redirect('todo_list')
