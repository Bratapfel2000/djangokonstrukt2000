from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tictactoeView(request):
	return render(request, 'tictactoe_js.html')
