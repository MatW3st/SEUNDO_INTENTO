from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('hello/<str:username>', views.hello,name="hello"),
    path('project/',views.projects,name="project"),
    path('project/<int:id>',views.project_detail,name="project_detail"),
    path('task/',views.task,name="task"),
    path('create_task/',views.create_task,name="create_task"),
    path('create_project/',views.create_project,name="create_project"),
    path('',include('pwa.urls')),
]
