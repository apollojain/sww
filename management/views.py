from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from .forms import *
from django.utils import timezone
from datetime import datetime, timedelta



def index(request):
	events_list = Event.objects.all()
	template = loader.get_template('index.html')
	context = {
		'events_list': events_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	try: 
		event = Event.objects.get(pk=event_id)
		prev_date = timezone.now() - timedelta(days = 2)
	except Event.DoesNotExist:
		raise Http404("Event does not exist")
	return render(request, 'detail.html', {'event': event})
