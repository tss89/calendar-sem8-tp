from django.conf.urls import url
from .views import logout

urlpatterns = [
    url(r'^flogin/logout/$', logout, name='logout'),
]
