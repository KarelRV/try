from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):  #Python 3.3 is going to use __str__
		return self.email


class Contact(models.Model):
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	email = models.EmailField()
	message = models.CharField(max_length = 255, blank = False, null = True)

	def __unicode__(self):
		return self.email