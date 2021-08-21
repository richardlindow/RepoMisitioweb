from django.contrib import admin
from .models import FirstClass

# Register your models here.

class FirstClassAdmin(admin.ModelAdmin):
	list_display = [ 'id' , 'columna1', 'columna2']

admin.site.register(FirstClass, FirstClassAdmin) # es importante primero definir la clase y al final registrarla