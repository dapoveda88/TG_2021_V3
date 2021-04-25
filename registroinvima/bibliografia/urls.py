from django.urls import path
from .import views

app_name = 'bibliografia'

urlpatterns = [
	path('lista_bib/',views.lista_bib, name ='lista_bib'),
]