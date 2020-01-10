from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def section_1View(request):
	return render(request, 'section_1.html')

