from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from polls.models import *
# Create your views here.

def index(request):
	return render_to_response('index.html')

def newreview(request):
	c = {}
	c.update(csrf(request))
	if request.POST:
		name=request.POST['name']
		year=request.POST['year']
		rating=int(request.POST['rating'])
		comment=request.POST['comment']
		addons=request.POST['addons']
		print name,year,rating,comment,addons
		newreview=Review(name=name,comment=comment,addons=addons,year=year,rating=rating)
		newreview.save()
		return HttpResponseRedirect('/')
	return render_to_response('newloc.html',context_instance=RequestContext(request))