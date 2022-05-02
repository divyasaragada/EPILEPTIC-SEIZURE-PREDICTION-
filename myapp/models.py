from django.db import models
from django.db.models import Model 
class user(models.Model):
	name = models.CharField(max_length=60)
	media = models.FileField(upload_to='myapp/static/upload',null=True)
# Create your models here.
