from django.shortcuts import render

# Create your views here.


def isfView(request):
	return render(request, "isf/isf.html")