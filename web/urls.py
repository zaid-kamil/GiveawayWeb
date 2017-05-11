from django.conf.urls import url

from web.views import show_home

urlpatterns = [
    url(r'^$', show_home,name='home'),
]
