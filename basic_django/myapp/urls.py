from django.urls import path
from django.views import View

from . import views

urlpatterns=[ path("",views.home,name="home"),path("base/",views.base,name="base"),
              path("add/",views.result)

                        ]
                        

