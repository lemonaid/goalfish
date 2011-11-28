from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.views import logout
from django.forms.models import modelformset_factory
import logging

def index(request):
	"""renders the default view, the / URI"""
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def logoout(request):
	"""logs out a user and returns them to /"""
	logout(request)
	
	return render_to_response('logout.html', {}, context_instance=RequestContext(request))
