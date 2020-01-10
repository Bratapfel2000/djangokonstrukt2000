
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.



def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html',	{'all_items': all_todo_items})

def addTodo(request):
	#create a new to do all_items
	new_item = TodoItem(content = request.POST['content'])
	#save
	new_item.save()
	#redicrect the browser to '/todo/'
	return HttpResponseRedirect('/todo/')

"""
def delete_todo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/todo/')
	"""

#anderes file
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
