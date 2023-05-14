from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index,name='index'),
    path('add/', views.add,name='add'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('delete/<int:id>/', views.delete,name='delete')
]