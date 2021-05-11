from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/review
    path('', views.index, name="index"),
]