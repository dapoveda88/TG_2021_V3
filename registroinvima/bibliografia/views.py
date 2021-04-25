from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import bib

def lista_bib (request):
	form = bib()
	context = {'lista':form}
	return render (request, "bibliografia/lista_bib.html",context)
	#return HttpResponse("esta es la bibliografia")

