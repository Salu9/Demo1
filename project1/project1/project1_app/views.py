from django.shortcuts import render, redirect

# Create your views here.
from .forms import Todoforms
from  . models import task


def add(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority,date=date)
        task1.save()

    return render(request,'home.html',{'task':task2})
#def details(request):

   # return render(request,'details.html',{'task':task1})
def delete(request,taskid):
    if request.method=='POST':
        task1 = task.objects.get(id=taskid)
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task1=task.objects.get(id=id)
    f=Todoforms(request.POST or None,instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task1})
