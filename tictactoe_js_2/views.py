from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tictactoe2View(request):
	return render(request, 'tictactoe_js_2.html')
