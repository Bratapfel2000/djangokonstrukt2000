from django.shortcuts import render
from django.http import HttpResponse

def w3_sandbox_1View(request):
	return render(request, 'w3_sandbox_1.html')
	#return HttpResponse("Hallo")