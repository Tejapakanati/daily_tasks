from django.urls import path
from .import views

urlpatterns = [
    path("",views.home, name="home"),
    path("tasks/", views.task_list , name="task_list"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
    path("delete/<int:id>/", views.delete_list_item, name="delete_list_item")

]