from django.urls import path, include
from .views import *

urlpatterns = [
    path("todos/", TodosView.as_view(), name="todo-list"),
    path("todos/<int:pk>/", TodoView.as_view(), name="todo-detail"),
]