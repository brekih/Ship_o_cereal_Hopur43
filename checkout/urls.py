from django.urls import path, include
from . import views

urlpatterns = [
    path('contact-information', views.contact, name='contact-index'),
    path('payment', views.payment, name='payment-index'),
    path('review', views.review, name='review-index'),
    path('confirm', views.confirm, name='confirm-index'),
    path('confirm-process', views.confirmProcess, name='confirm-process-index')
]