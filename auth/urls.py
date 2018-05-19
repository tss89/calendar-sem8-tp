from django.conf.urls import url

from .views import token

urlpatterns = [
    url(r'^flogin/token/$', token, name='token'),
]
