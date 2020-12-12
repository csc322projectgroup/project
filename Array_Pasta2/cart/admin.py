from django.contrib import admin
from .models import menu1, menu2


class Menu1Admin(admin.ModelAdmin):
	list_display = ('name', 'price')
admin.site.register(menu1, Menu1Admin)

class Menu2Admin(admin.ModelAdmin):
	list_display = ('name', 'price')
admin.site.register(menu2, Menu2Admin)

