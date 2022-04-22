from django.urls import path
from mainapp.views import get_city, acknowledge

urlpatterns = [
    path('', get_city, name='index'),
    path('acknowledgement', acknowledge, name="acknowledgement"),
]