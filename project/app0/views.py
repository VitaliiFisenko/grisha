from django.shortcuts import render
from django.http import HttpResponse
import time

def index(request):
	
	return HttpResponse("<h1 align='center' style='color:red; font-size:50px;'>WELL DONE!</h1>")
# Create your views here.
