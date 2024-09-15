from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/', views.tasks),
    path('preparation/', views.preparation_materials),

]
