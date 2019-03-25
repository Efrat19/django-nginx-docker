from django.shortcuts import render
from django.http import HttpResponse
from emoji.models import Emoji
from django.template import loader, RequestContext
from django.core.serializers import serialize


# Create your views here.


def index(request):
	template = loader.get_template('emoji/index.html')
	context = RequestContext(request, {
		'title': 'emoji #1'
	})
	return HttpResponse(template.render())


def get_list(request):
	return HttpResponse(serialize('json', Emoji.objects.all()))
