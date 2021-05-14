from django.shortcuts import render, redirect
from cartapp.models import tableCart

# Create your views here.

def contact(request):
    return render(request, 'checkout/contact.html')

def payment(request):
    return render(request, 'checkout/payment.html')

def review(request):
    context = {'cart': tableCart.objects.all()}
    return render(request, 'checkout/review.html', context)

def confirm(request):
    return render(request, 'checkout/confirmation.html')

def confirmProcess(request):
    obj = tableCart.objects.all()
    obj.delete()
    return redirect('confirm-index')