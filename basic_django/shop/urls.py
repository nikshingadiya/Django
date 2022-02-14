from django.urls import path
from django.views import View

from . import views

urlpatterns=[ path("",views.index,name="index"),path("index.html",views.index_2,name="index_2"),
              path("index/shop",views.shop,name="shop"),
              path("index/why",views.why,name="why"),
              path("index/contact",views.contact,name="contact"),
              path("index/testimonial",views.testimonial,name="testimonial")]
                        

