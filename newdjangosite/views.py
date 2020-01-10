from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newdjangositeView(request):
	return render(request, 'newdjangosite.html')
	#return HttpResponse("Hallo")