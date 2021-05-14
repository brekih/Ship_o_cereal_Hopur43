from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from cereal.forms.cereal_form import CerealCreateForm, CerealUpdateForm
from cereal.models import Cereal, CerealImage


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        cereals = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstimage': x.cerealimage_set.first().image
        } for x in Cereal.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({'data': cereals })
    context = {'cereals': Cereal.objects.all().order_by('name')}
    return render(request, 'cereal/index.html', context )


def get_cereal_by_id(request, id):
    return render(request, 'cereal/cereal_details.html', {
        'cereal':get_object_or_404(Cereal, pk=id)
    })
@login_required
def create_cereal(request):
    if request.method == 'POST':
        form = CerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            cereal_image = CerealImage(image=request.POST['image'], cereal=cereal)
            cereal_image.save()
            return redirect('cereal-index')

    else:
        form = CerealCreateForm()
    return render(request, 'cereal/create_cereal.html', {
        'form': form
    })
@login_required
def delete_cereal(request, id):
    cereal = get_object_or_404(Cereal, pk=id)
    cereal.delete()
    return redirect('cereal-index')
@login_required
def update_cereal(request, id):
    instance = get_object_or_404(Cereal, pk=id)
    if request.method == 'POST':
        form = CerealUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cereal_details', id=id)
    else:
        form = CerealUpdateForm(instance=instance)
    return render(request, 'cereal/update_cereal.html', {
        'form': form,
        'id' : id
    })

def cereal_products(request, id):
    if id != 0:
        context = {'cereals': Cereal.objects.filter(is_merch=False, category_id=id).all().order_by('name')}
    else:
        context = {'cereals': Cereal.objects.filter(is_merch=False).all().order_by('name')}
    return render(request, 'cereal/index.html', context )

def merch_products(request, id):
    if id != 0:
        context = {'cereals': Cereal.objects.filter(is_merch=True, category_id=id).all().order_by('name')}
    else:
        context = {'cereals': Cereal.objects.filter(is_merch=True).all().order_by('name')}
    return render(request, 'cereal/index.html', context )

def sort(request, id):
    if id == 1:
        context = {'cereals': Cereal.objects.all().order_by('name')}
    elif id == 2:
        context = {'cereals': Cereal.objects.all().order_by('-name')}
    elif id == 3:
        context = {'cereals': Cereal.objects.all().order_by('price')}
    elif id == 4:
        context = {'cereals': Cereal.objects.all().order_by('-price')}
    else:
        context = {'cereals': Cereal.objects.all()}
    return render(request, 'cereal/index.html', context )