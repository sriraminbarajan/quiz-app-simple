from django.conf.urls import url,include
from django.contrib import admin
from . import views


#defining the path 
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login_request, name="login"),
    url(r'^logout', views.logout_request, name="logout"),
    url(r'^about', views.about, name = 'about'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
