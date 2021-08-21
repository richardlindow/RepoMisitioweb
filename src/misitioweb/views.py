from django.shortcuts import render

def inicio(request):
	template_name = 'inicio.html'
	ctx = {
		'variable': 'si estás leyendo esto te merecés un descanso'
	}
	return render(request, template_name, ctx)
