from django.forms import ModelForm, widgets
from cartapp.models import tableCart

class ItemAddForm(ModelForm):
    class Meta:
        model = tableCart
        exclude = ['id']
        widgets = {
            'CerealAmount':widgets.TextInput(attrs= {'class': 'form-control', 'placeholder': '0'}),
            'IdCereal': widgets.TextInput(attrs= {'class': 'form-control', 'placeholder': '0'})
        }