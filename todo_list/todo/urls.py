from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView
# from .views import *

app_name = 'todo'

urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', TodoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
]