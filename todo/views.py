from django.shortcuts import render, redirect

from todo.forms import *


# Create your views here.


def registration(request):
    error = None
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid() and 'register' in request.POST:
            users = User.objects.filter(username=request.POST['username'])

            if users:
                error = 'Username already exists'
            else:
                fm.save()
                user_id = User.objects.latest('id')
                return redirect(index, user_id)

        elif fm.is_valid():
            users = User.objects.all()
            exists = False
            user_id = 0
            for user in users:
                if user.username == request.POST['username'] \
                        and user.password == request.POST['password']:
                    exists = True
                    user_id = user.id
                    break

            if exists:
                return redirect(index, user_id)

            else:
                error = 'Your username or password is wrong'

    else:
        fm = UserForm()

    return render(request, 'registration.html', {'fm': fm, 'error': error})


def index(request, user_id):
    tasks = Task.objects.filter(user_id=user_id)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index, user_id)

    context = {'tasks': tasks, 'form': form, 'id': user_id}
    return render(request, 'list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(index, task.user_id)

    context = {'form': form, 'user_id': task.user_id}
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect(index, task.user_id)

    context = {'item': task, 'user_id': task.user_id}
    return render(request, 'delete.html', context)
