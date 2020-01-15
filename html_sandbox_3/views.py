from django.shortcuts import render
from django.http import HttpResponse

def html_sandbox_3View(request):
	return render(request, 'html_sandbox_3.html')
	#return HttpResponse("Hallo")