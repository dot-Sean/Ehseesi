from django.conf.urls import patterns, url

from EhseesiApp import views

urlpatterns = [
    url(r'search', 'EhseesiApp.mysite.EhseesiApp.urls'),
    url(r'results', 'EhseesiApp.mysite.EhseesiApp.urls'),
    url(r'admin/', 'EhseesiApp.mysite.EhseesiApp.urls'),
]