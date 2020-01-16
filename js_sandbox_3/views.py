from django.shortcuts import render
from django.http import HttpResponse

def js_sandbox_3View(request):
	return render(request, 'js_sandbox_3.html')
