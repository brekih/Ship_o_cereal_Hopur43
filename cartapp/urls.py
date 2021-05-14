from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('addItem/<int:id>', views.addItem, name="cart-add"),
    path('removeItem/<int:id>', views.removeItem, name="cart-remove"),
]