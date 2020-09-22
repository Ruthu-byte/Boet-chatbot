from django.conf.urls import url
from django.contrib import admin
from . import views1


urlpatterns = [
    url(r'^$', views1.ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbot/', views1.ChatterBotApiView.as_view(), name='chatterbot'),
]
