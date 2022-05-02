from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def index(request):

    tasks=Task.objects.all()
    

    content={"tasks":tasks}
    return render(request,"index.html",content)

def add(request):
    if(request.method=='POST'):
        task=Task()
        task.title=request.POST.get("title")
        task.save()
    
    return redirect('/')

def delete(request,pk):
    if(request.method=='POST'):
        task=Task.objects.get(id=pk)
        task.delete()
    return redirect('/')

def update(request,pk):
    try:
        task=Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return redirect('/')
    if(request.method=='POST'):    
        task.title=request.POST.get("title")
        if(request.POST.get("check")):
            task.is_complete=True
        else:
            task.is_complete=False
        task.save()
        return redirect('/')        
    content={"task":task}
    return render(request,"update.html",content)