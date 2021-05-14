from django.shortcuts import render, get_object_or_404, redirect
from cartapp.models import tableCart
from cereal.models import Cereal

# Create your views here.
def index(request):
    context = {'cart': tableCart.objects.all()}
    return render(request, 'cart/index.html', context)

def addItem(request, id):
    try:
        obj = tableCart.objects.get(IdCereal=id)
    except tableCart.DoesNotExist:
        obj = None
    if obj == None:
        Item = tableCart.objects.create(IdCereal=(Cereal.objects.get(pk=id)),CerealAmount=1)
    else:
        obj.CerealAmount += 1
        obj.save()
    return redirect('cereal-index')

def removeItem(request, id):
    Item = get_object_or_404(tableCart, IdCereal=id)
    Item.delete()
    return redirect('cart-index')