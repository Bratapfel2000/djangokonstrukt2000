from django.shortcuts import render
from django.http import HttpResponse

def w3_sandbox_3View(request):
	return render(request, 'w3_sandbox_3.html')
	#return HttpResponse("Hallo")