from django.shortcuts import render
from django.http import HttpResponse

def pagina_ppal (request):
	return render (request, "principal/main.html")
	#return HttpResponse("Hola mundo")

# Create your views here.
