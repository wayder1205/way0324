from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
	myname = "黃偉桐"
	data = [i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = [6]
	return render(request, 'index.html', locals())
# Create your views here.
