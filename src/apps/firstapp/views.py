from django.shortcuts import render

# Create your views here.

from .models import FirstClass

def firstView(request):
	template_name = 'firstapp/first.html'
	lista_objects = FirstClass.objects.all()
	ctx = {
		'variable': 'algo anda, dame un mes mas',
		'lista': lista_objects
	}
	return render(request, template_name, ctx)