from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from django.forms.models import modelformset_factory
import logging

def index(request):
	
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
