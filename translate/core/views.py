from django.shortcuts import render,redirect
from .forms import SignupForm
# Create your views here.
def index(request):
    return redirect("tasks:all_tasks")

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form =SignupForm()
    return render(request,'core/signup.html',{'form':form})