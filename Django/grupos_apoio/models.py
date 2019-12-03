from django.db import models

class Cadastro_grupos(models.Model):
	"""Essa classe irá conter os dados necessários 
	para o cadastro dos grupos de apoio para o auxílio das mulheres"""
	nome_grupo = models.CharField(max_length = 50)
	rua = models.CharField(max_length = 30)
	bairro = models.CharField(max_length = 30)
	numero = models.IntegerField()
	email = models.EmailField(max_length = 75) #email para contato
	blog = models.URLField(max_length = 200) #url para algum site e/ou blog
	bio = models.TextField()
		
