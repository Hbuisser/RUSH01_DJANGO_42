from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	surname = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	description = models.TextField()
	profil_picture = models.ImageField(upload_to='img/')

	def __str__(self):
		return str(self.name)
