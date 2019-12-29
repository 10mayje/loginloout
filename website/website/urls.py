
from django.conf.urls import url,include
from django.contrib import admin
from account import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',user_views.home,name='23'),
    url(r'^account/',include('account.urls')),


]
