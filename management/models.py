from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
def event_directory_path(instance, filename):
	    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	    return 'event_{0}/{1}'.format(instance.event.id, filename)


class Event(models.Model):
	'''
		name, datetime, description, facilitator, attendees, archive
	''' 
	name = models.CharField(max_length=200)
	facilitator = models.ForeignKey(User, related_name="facilitator")
	extension = models.IntegerField()
	datetime = models.DateTimeField()
	description = models.TextField(max_length=2000, blank=True, null=True)
	archive = models.FileField(upload_to=event_directory_path, blank=True, null=True)
	def __str__(self):
		return str(self.name) + " | " + str(self.facilitator.username)
	
class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	events = models.ForeignKey(Event, related_name="events")
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=11) # validators should be a list
	admin = models.BooleanField(default=False)
	def __str__(self):
		return str(self.first_name) + " " + str(self.last_name)
	