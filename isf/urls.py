from django.urls import path
from .views import isfView


urlpatterns = [
    path('', isfView),
            ]
