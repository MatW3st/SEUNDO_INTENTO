#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title = 'Django Curse!!'
    return render(request,'index.html',{'title':title})

def hello (request,username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username='Cartormech'
    return render(request,'about.html',{'username':username})

def projects(request):
    projects = list( Project.objects.all())
    return render(request,'project/projects.html',{'projects':projects})

def task(request):
    #task= get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request,'tasks/tasks.html',{'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        #show interface
        return render(request,'tasks/create_task.html',{'form':CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],descripcion=request.POST['descripcion'],project_id=2)
        return redirect('task')
    
def create_project(request):
    if request.method == 'GET':
        return render(request,'project/create_project.html',{'form':CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')
    
def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=id)
    return render(request,'project/detail.html',{'project':project, 'tasks':tasks})