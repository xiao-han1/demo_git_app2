from django.urls import path
from .views import *

urlpatterns = [
    path("index/",index_s,name = "index_s")
]