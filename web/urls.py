from django.conf.urls import url

from web.views import show_home, view_contact, show_about

urlpatterns = [
    url(r'^$', show_home, name='home'),
    url(r'^contact/$', view_contact, name='contact'),
    url(r'^about$', show_about, name='about')
]

