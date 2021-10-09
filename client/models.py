from django.db import models

# Create your models here.
class UserDetails(models.Model):
	name = models.CharField(max_length=500)
	email = models.CharField(max_length=500)
	companyname = models.CharField(max_length=500)