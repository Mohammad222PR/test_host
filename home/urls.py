from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.connect_to_database, name="connect_to_database"),
    path("<int:pk>", views.delete_task, name="delete_task"),

]
