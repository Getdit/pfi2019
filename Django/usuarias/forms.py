from django.forms import ModelForm 
from .models import Cadastro

def Cadastrodenuncias(ModelForm):
	class Meta:
		model = 'POST'
		fields = ('first_name', 'last_name', 'age', 'descricao')
