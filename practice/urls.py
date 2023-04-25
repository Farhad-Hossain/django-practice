from django.urls import path
from . import views 





urlpatterns = [
    path('/abc', views.index),
    path('/create-model', views.create_model, name="create_model"),
]