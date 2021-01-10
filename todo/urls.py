from django.urls import path

from todo import views

urlpatterns = [
    path('list/<str:user_id>/', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('', views.registration, name="login"),
]
