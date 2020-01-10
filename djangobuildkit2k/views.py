from django.shortcuts import render
from django.http import HttpResponse

def djangobuildkit2kView(request):
	return render(request, 'djangobuildkit2k.html')
	#return HttpResponse("Hallo")