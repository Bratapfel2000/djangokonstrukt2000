from django.shortcuts import render
from django.http import HttpResponse

#def todo_1_View(request):
#	return HttpResponse("Hello this is the test to do")


def todo_2_View(request):
	return render(request, 'todo_2.html')