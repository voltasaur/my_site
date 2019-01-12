from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	#print (dir(HttpResponse))
	#print (dir(HttpResponse.content.setter))
	return HttpResponse(" Hello, world. You're at the polls index. ")