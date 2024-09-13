from django.urls import path
from . import views


app_name = 'Todo'

urlpatterns = [
    path('', views.TodoView, name='Todo'),
    path('Detail/<int:todo_id>/', views.TodoDetailView, name='Detail'),
    path('Create/', views.TodoCreate, name='Create'),
    path('Delete/<int:todo_id>/', views.TodoDelete, name='Delete'),
    path('Update/<int:todo_id>/', views.TodoUpdate, name='Update')
]