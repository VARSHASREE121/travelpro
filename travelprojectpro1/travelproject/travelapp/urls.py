from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
]
"""path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('thank/',views.thank,name='thank'),
    path('about/',views.about,name='about'),
    path('add/',views.finalans,name='finalans'),
    path('home/add/',views.finalans,name='finalans')"""

