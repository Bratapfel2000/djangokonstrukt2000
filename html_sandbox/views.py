from django.shortcuts import render
from django.http import HttpResponse

def html_sandboxView(request):
	return render(request, 'html_sandbox.html')
	#return HttpResponse("Hallo")