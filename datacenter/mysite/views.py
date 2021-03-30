from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	myname = "黃偉桐"
	return render(request, 'index.html', locals())
# Create your views here.
