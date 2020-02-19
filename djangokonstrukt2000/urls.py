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
from tictactoe_js_2.views import tictactoe2View
from djangobuildkit2k.views import djangobuildkit2kView
from html_sandbox.views import html_sandboxView
from html_sandbox_2.views import html_sandbox_2View
from html_sandbox_3.views import html_sandbox_3View
from todo_1.views import todo_1_View
from todo_2.views import todo_2_View
from w3_sandbox_1.views import w3_sandbox_1View
from w3_sandbox_2.views import w3_sandbox_2View
from w3_sandbox_3.views import w3_sandbox_3View
from js_sandbox_1.views import js_sandbox_1View
from js_sandbox_2.views import js_sandbox_2View
from js_sandbox_3.views import js_sandbox_3View

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
    path('tictactoe_js_2/',tictactoe2View),
    path('djangobuildkit2k/', djangobuildkit2kView),
    path('html_sandbox/', html_sandboxView),
    path('html_sandbox_2/', html_sandbox_2View),
    path('html_sandbox_3/', html_sandbox_3View),
    path('todo_1/', todo_1_View),
    path('todo_2/', todo_2_View),
    path('w3_sandbox_1/', w3_sandbox_1View),
    path('w3_sandbox_2/', w3_sandbox_2View),
    path('w3_sandbox_3/', w3_sandbox_3View),
    path('js_sandbox_1/', js_sandbox_1View),
    path('js_sandbox_2/', js_sandbox_2View),
    path('js_sandbox_3/', js_sandbox_3View),
            ]
