from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^song/',views.new,name='new'),
    url(r'^test/',views.test,name='test'),
    url(r'^login/', views.login, name='log'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^reg/',views.reg,name='reg'),



]
