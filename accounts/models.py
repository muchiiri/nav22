from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):

	def create_superuser(self, email, firstname, lastname, password=None, **other_fields):
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser',True)
		other_fields.setdefault('is_active', True)

		return self.create_user(email, firstname, lastname, password, password, **other_fields)


	def create_user(self, email, firstname, lastname,company, password, **other_fields):
		if not email:
			raise ValueError(_('You must provide an email address'))

		email = self.normalize_email(email)
		user = self.model(email=email,firstname=firstname,lastname=lastname,**other_fields)
		user.set_password(password)
		user.save()
		return user

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('Email address'), unique=True)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	company = models.CharField(max_length=1000)
	address = models.CharField(max_length=200,blank=True)
	start_date = models.DateField(default=timezone.now)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	objects = CustomAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['firstname', 'lastname',]

	def __str__(self):
		return self.email
