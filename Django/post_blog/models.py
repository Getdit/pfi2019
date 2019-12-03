from django.conf import settings
from django.db import models
from django.utils import timezone

class Texto_blog(models.Model):
	"""classe necessária para fazer os post do blog
	com os textos da psico"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title


