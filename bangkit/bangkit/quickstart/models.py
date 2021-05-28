from django.db import models

# Create your models here.

class classificationModel(models.Model):
	judul = models.CharField(max_length=250)
	location = models.CharField(max_length=50)
	image = models.ImageField(upload_to='poto')
	time = models.DateTimeField(auto_now_add=True)