from django.db import models
from django.utils import timezone


class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	crear_dia = models.DateTimeField(
			default = timezone.now)
	publicar_dia = models.DateTimeField(
			blank = True, null= True)

def publicar(self):
	self.publicar_dia = timezone.now()
	self.save()

def __str__(self):
	return self.titulo

