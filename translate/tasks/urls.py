from django.urls import path

from . import views

app_name= 'tasks'
urlpatterns = [
    path('new/',views.new,name='new'),
    path('usertasks/',views.user_tasks,name='user_tasks'),
    path("<int:pk>/",views.details,name='details'),
    path('all/',views.all_tasks,name='all_tasks'),
    path("<int:pk>/manage",views.manage_answer,name='manage_answer')
]