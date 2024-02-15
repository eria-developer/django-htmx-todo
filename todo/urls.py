from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home")
]

htmx_patterns = [
    path("clear_message/", views.clear_message, name="clear_message"),
    path("create_todo/", views.create_todo, name="create_todo"),
    path("delete_todo/<int:pk>", views.delete_todo, name="delete_todo"),
    path("mark_todo/<int:pk>", views.mark_todo, name="mark_todo"),
    path("todo_details/<int:pk>", views.todo_details, name="todo_details")
]

urlpatterns += htmx_patterns