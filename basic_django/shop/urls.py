from django.urls import path
from django.views import View

from . import views

urlpatterns=[ path("",views.index,name="index"),path("static/index.html",views.index_2,name="index_2")]
                        

