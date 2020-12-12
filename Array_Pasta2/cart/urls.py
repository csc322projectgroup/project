from django.urls import path
from . import views

urlpatterns = [
	path('cart/', views.view_cart, name = 'view_cart'),
    path('menu/', views.menu_list_view, name = 'menu_list'),
	path('menu1/', views.menu1_view, name = 'menu1'),
	path('menu2/', views.menu2_view, name = 'menu2')
]