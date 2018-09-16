from django.conf.urls import url
from django.urls import path

from .views import get_home, get_items

urlpatterns = [
    path('', get_home, name='home'),
    url(r'^category/(?P<slug>[-\w]+)/$', get_items, name='category')
]