from django.shortcuts import render
from .models import menu1, menu2

# Create your views here.
def view_cart(request):
	return render(request, 'cart/view_cart.html')

def menu_list_view(request):
	return render(request, 'cart/menu_list.html')
	
def menu1_view(request):
	items = menu1.objects.all()
	ctx = {'items': items}
	return render(request, 'cart/menu1.html', ctx)
	
def menu2_view(request):
	items = menu2.objects.all()
	ctx = {'items': items}
	return render(request, 'cart/menu2.html', ctx)