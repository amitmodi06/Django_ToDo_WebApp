from django.urls import path
from . import views

urlpatterns = [
    path("", views.displayToDo, name="displayToDo")
]
