from django.shortcuts import render, redirect
from django.contrib import messages as msg
from . models import TodoModel
from . forms import TodoCreationForm, TodoUpdateForm


def TodoView(request):
    Todos = TodoModel.objects.all()
    return render(request, 'Todo/Todo.html', {'Todos': Todos})

def TodoDetailView(request, todo_id):
    TodoDetail = TodoModel.objects.get(id=todo_id)
    return render(request, 'Todo/Detail.html', {'TodoDetail': TodoDetail})

def TodoCreate(request):
    if request.method == 'POST':
        form = TodoCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            NewTodo = TodoModel.objects.create(title=cd['title'], todolist=cd['todolist'], textarea=cd['textarea'], Done=cd['Done'], created=cd['created'])
            msg.success(request, f'{cd["title"]} Was Created', 'success')
            return redirect('Todo:Detail', NewTodo.id)

    else:
        form = TodoCreationForm
    return render(request, 'Todo/Create.html', {'forms': form})

def TodoDelete(request, todo_id):
    TodoDelete = TodoModel.objects.get(id=todo_id)
    TodoDelete.delete()
    msg.error(request, f'{TodoDelete} Was Deleted', 'danger')
    return redirect('Todo:Todo')


def TodoUpdate(request, todo_id):
    Todo = TodoModel.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=Todo)
        if form.is_valid():
            form.save()
            msg.success(request, f"{Todo.title} was updated successfully", 'info')
            return redirect('Todo:Detail', Todo.id)
    else:
        form = TodoUpdateForm(instance=Todo)
    return render(request, 'Todo/Update.html', {'form': form})