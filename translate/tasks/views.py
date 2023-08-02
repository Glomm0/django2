from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTaskForm,EditTaskForm,NewTakenForm
from .models import Task,TakenTask
from django.db.models import Q
# Create your views here.

@login_required
def new(request):
    if request.method=='POST':
        form=NewTaskForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.created_by=request.user
            form.save()
            return redirect('core:index')
    else:
        form=NewTaskForm()

    return render(request,'tasks/form.html',{'form':form,'title':'New task'})
@login_required
def user_tasks(request):
    user_tasks=Task.objects.filter(created_by=request.user)
    
    return render(request,"tasks/usertasks.html",{"user_tasks":user_tasks})

@login_required
def details(request,pk):
    task =get_object_or_404(Task,pk=pk)
    answers=TakenTask.objects.filter(taken_task=task)
    if request.method=="POST":
        if request.user==task.created_by:
            form=EditTaskForm(request.POST,instance=task)
            if form.is_valid():
                form=form.save(commit=False)
                form.created_by=request.user
                form.save()
                return redirect('tasks:details',pk=task.id)
        else:
            form=NewTakenForm(request.POST)
            if form.is_valid():
                form=form.save(commit=False)
                form.taken_by=request.user
                form.taken_task=task
                form.save()
                
                return redirect('tasks:details',pk=task.id)
    else:
        if request.user==task.created_by:
            form=EditTaskForm(initial={'text':task.text})
        else:
            form=NewTakenForm()
        
    return render(request,"tasks/details.html",{"task":task,"form":form,"answers":answers})

def all_tasks(request):
    tasks=Task.objects.filter(is_done=False)
    return render(request,"tasks/tasks.html",{"tasks":tasks})

@login_required
def manage_answer(request,pk):
    decision=request.GET.get('decision','')
    taken_task=get_object_or_404(TakenTask,pk=request.GET.get('taken_task',0))
    task =get_object_or_404(Task,pk=pk)
    if decision=='accept':
        task.is_done=True
        answers=TakenTask.objects.filter(taken_task=task).exclude(id=taken_task.id).delete()
        task.save()
    else:
        taken_task.delete()
    return redirect('tasks:details',pk=pk)