from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/', views.tasks_main_page),
    path('tasks/<int:task_id>/', views.tasks),
    path('preparation/', views.preparation_materials),

]
