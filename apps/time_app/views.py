from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	context = {
	"time": strftime("%d-%m-%Y %H:%M %p", gmtime())
	}
	return render(request, 'time_app/index.html', context)


