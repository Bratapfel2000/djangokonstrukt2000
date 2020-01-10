from django.shortcuts import render
from django.http import HttpResponse

def css_sandboxView(request):
	return render(request, 'css_sandbox.html')
	#return HttpResponse("Hallo")