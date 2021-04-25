from django import forms

class bib (forms.Form):
	tipo = forms.CharField(label='tipo de publicación', )
	titulo = forms.CharField(label='titulo de la referencia', help_text ='prueba')
	autor = forms.CharField(label='Nombre Autor')
	revista = forms.CharField(label='Revista')


