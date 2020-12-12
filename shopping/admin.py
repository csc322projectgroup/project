from django.contrib import admin
from .models import Menu
from .models import Item
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('menuId','cheffName','date_made')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price','menu')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)