from django.contrib import admin

from .models import User, Event, Person

admin.site.register(Event)
admin.site.register(Person)