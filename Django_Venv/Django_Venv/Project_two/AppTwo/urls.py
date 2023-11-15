from django.urls import path
from . import views

urlpatterns = [
    path('AppTwo/', views.AppTwo, name='AppTwo'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]