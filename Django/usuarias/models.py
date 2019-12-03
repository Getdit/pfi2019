from django.db import models

class Cadastro(models.Model):
	"""Esta classe irá receber os dados necessários para 
	criar um cadastro das usuárias na hora de fazer uma denúncia"""
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	age = models.IntegerField()
	descricao = models.TextField()
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	
class Desabafo(models.Model):
	"""classe que contem os campos necessários para a área de desabafos"""
	nome = models.CharField(max_length=30)
	texto = models.TextField()
