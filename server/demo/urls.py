from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dictionary', views.d),
    path('dictionary2', views.d2),
    path('filter', views.fil),
    path('filter2', views.fil2),
    path('filter3', views.fil3),
    path('get_company', views.get_company),
    path('get_company_values', views.get_company_values),
    re_path(
        r'^company-autocomplete/$',
        views.CompanyAutoComplete.as_view(),
        name='company-autocomplete',
    ),
]