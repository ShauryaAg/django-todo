from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForms, NewTodoForm


# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')

    # form = TodoForms()
    newtodoform = NewTodoForm()

    context = { 'todo_list': todo_list, 'form': newtodoform }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    # if request.method == 'POST':
    # form = TodoForms(request.POST)
    newtodoform = NewTodoForm(request.POST)

    if newtodoform.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        newtodoform.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')