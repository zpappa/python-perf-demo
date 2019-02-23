from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dictionary', views.d),
    path('dictionary2', views.d2),
    path('filter', views.fil),
    path('filter2', views.fil2),
    path('filter3', views.fil3),
]