from django.shortcuts import render
from .models import Item
#from django.http import HttpResponse
# Create your views here.

def home(request):
    print(request)
    items = Item.objects.all()
    ctx = {'items': items}
    return render(request, 'shopping/menu.html',ctx)



