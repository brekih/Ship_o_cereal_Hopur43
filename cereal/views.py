from django.shortcuts import render

cereals = [
    {'name': 'Cheerios', 'price': 4.99 , 'image':'https://www.cheerios.com/wp-content/uploads/2018/04/YBC_460x460.png', 'description':'The one and only Cheerios, we all know and love'},
    {'name': 'Cocoa Puffs', 'price': 5.99 , 'image':'https://i5.wal.co/asr/c4913f0b-76de-45ef-9abd-96697cf28d5c.fed751aa40ec00346d297d49849571c5.png?odnWidth=1000&odnHeight=1000&odnBg=ffffff ', 'description':'Im crazy for cocoa puffs.'},
    {'name': 'Lucky Charms', 'price': 6.99 , 'image':'https://res.cloudinary.com/general-mills/image/upload/q_auto,f_auto/luckyCharmsUS/wp-content/uploads/2020/02/original-460x460-1.png ', 'description':'Will mess up yo teeth.'},
    {'name': 'Trix', 'price': 4.99 , 'image':'https://e22d0640933e3c7f8c86-34aee0c49088be50e3ac6555f6c963fb.ssl.cf2.rackcdn.com/0016000275320_CL_Syndigo_default_large.png ', 'description':'Trix are for kids.'},
    {'name': 'Alpen', 'price': 3.99 , 'image':'https://www.postconsumerbrands.ca/wp-content/uploads/2018/08/Alpen-NSA-left-1.png ', 'description':'Wtf is Alpen.'},
    {'name': 'Gardr', 'price': 8.99 , 'image':''},
]


# Create your views here.
def index(request):
    return render(request, 'cereal/index.html', context={ 'cereals': cereals })