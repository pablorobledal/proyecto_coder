from django.urls import path
from AppUsers.views import *

urlpatterns = [
    path('', pablitoputo, name='pablito'),
    
]