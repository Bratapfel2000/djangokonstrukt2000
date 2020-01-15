from django.shortcuts import render
from django.http import HttpResponse

def w3_sandbox_2View(request):
	return render(request, 'w3_sandbox_2.html')
	#return HttpResponse("Hallo")