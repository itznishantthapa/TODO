from django.urls import path
from . import views

urlpatterns=[
    path('',views.todo_list,name='todo_list'),
    path('add/',views.add_note,name='add'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('edit/<int:pk>/',views.edit,name='edit'),
]