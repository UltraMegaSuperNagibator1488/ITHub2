from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('tasks/', views.tasks),
    path('theory/', views.theory),
    path('tasks/<slug:slug_id>', views.tasks_number),
]
