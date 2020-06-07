from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Attack
from django.template import loader

def index(request):
	latest_attack_list = Attack.objects.order_by('-attack_date')[:5]
	template = loader.get_template('ddos/index.html')
	context = {
		'latest_attack_list': latest_attack_list,
	}
	return HttpResponse(template.render(context,request))

def resources(request):
	ip_addresses = Attack.objects.order_by('-attack_date')[:5]
	template = loader.get_template('ddos/resources.html')
	context = {
		'ip_addresses': ip_addresses,
	}
	return HttpResponse(template.render(context,request))


def detail(request, attack_id):
	return HttpResponse("You are looking at attack %s." % attack_id)

def results(request, attack_id):
	response = "You are looking at the results of attack %s."
	return HttpResponse(response % attack_id)



