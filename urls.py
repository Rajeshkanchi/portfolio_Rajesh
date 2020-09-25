
from django.urls import path

from.import views

urlpatterns = [
    path('',views.first_page,name='first_page'),
    path('contact',views.contact,name='contact'),
    path('first_page',views.first_page,name='home'),
    path('About_Me',views.About_Me,name='About_Me'),
    path('Work',views.Work,name='Work'),



]