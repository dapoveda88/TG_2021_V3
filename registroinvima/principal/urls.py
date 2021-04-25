from django.urls import path
from .import views

app_name = 'principal'

urlpatterns = [
	path('',views.pagina_ppal, name ='pagina_ppal'),
]