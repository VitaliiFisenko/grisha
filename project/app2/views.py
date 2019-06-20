from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
	return HttpResponse('<h1 align="center" style="color:red; font-size:70px">BAT`A LOH</h1>')
# Create your views here.
