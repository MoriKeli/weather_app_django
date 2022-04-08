from django.urls import path
from mainapp.views import get_city
urlpatterns = [
    path('', get_city, name='index')
]