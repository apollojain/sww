from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from .forms import *
from .forms import *
from django.utils import timezone
from datetime import datetime, timedelta



def index(request):

	user_events_list = Event.objects.none()
	regular_events_list = Event.objects.all()
	if request.user.is_authenticated: 
		p_list = Person.objects.filter(user = request.user)
		if len(p_list) > 0: 
			p = p_list[0]
			user_events_list = p.events.all()
			user_pk_list = [item.pk for item in user_events_list]
			regular_events_list = Event.objects.exclude(pk__in=user_pk_list)
	template = loader.get_template('index.html')
	context = {
		'user_events_list': user_events_list,
		'regular_events_list': regular_events_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	try: 
		boolean = False
		event = Event.objects.get(pk=event_id)
		prev_date = timezone.now() - timedelta(days = 2)
		if request.user.is_authenticated: 
			p_list = Person.objects.filter(user = request.user)
			if len(p_list) > 0: 
				p = p_list[0]
				if len(p.events.filter(pk = event_id)) > 0: 
					boolean = True
	except Event.DoesNotExist:
		raise Http404("Event does not exist")
	return render(request, 'detail.html', {'event': event, "boolean": boolean})

def toggle(request, event_id):
	if request.user.is_authenticated: 
		p_list = Person.objects.filter(user = request.user)
		if len(p_list) > 0: 
			print "Checkpoint 3"
			p = p_list[0]
			qs = p.events.filter(pk = event_id)
			if len(qs) > 0: 
				p.events.remove(qs[0])
			else: 
				event = Event.objects.filter(pk = event_id)[0]
				p.events.add(event)
	return redirect('event_detail', event_id)

def create(request): 
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid(): 
			print form.cleaned_data
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			phone_number = form.cleaned_data.get('phone_number')
			user = User.objects.create_user(username, email, password)
			user.save
			person = Person(
				user=user, 
				first_name=first_name, 
				last_name=last_name, 
				phone_number=phone_number
			)
			person.save()
			return redirect('login')

	else: 
		form = UserForm()
	return render(request, 'new_user.html', {'form': form})
