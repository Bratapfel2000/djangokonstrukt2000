"""djangokonstrukt2000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from section_1.views import section_1View
from todo.views import todoView, addTodo, deleteTodo
from home.views import homeView
from newdjangosite.views import newdjangositeView
from css_sandbox.views import css_sandboxView
from tictactoe_js.views import tictactoeView
from djangobuildkit2k.views import djangobuildkit2kView
from html_sandbox.views import html_sandboxView
from todo_1.views import todo_1_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('section_1/', section_1View),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('home/', homeView),
    path('newdjangosite/', newdjangositeView),
    path('css_sandbox/',css_sandboxView),
    path('tictactoe_js/',tictactoeView),
    path('djangobuildkit2k/', djangobuildkit2kView),
    path('html_sandbox/', html_sandboxView),
    path('todo_1/', todo_1_View),

]
