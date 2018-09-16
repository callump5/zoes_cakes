from django.conf.urls import url
from django.urls import path

from .views import get_home

urlpatterns = [
    url(r'$', get_home, name='home'),
]