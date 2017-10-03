"""URL pattern definitions for Equipment App"""

from django.conf.urls import url
from . import views

app_name = 'customer'

urlpatterns = [
    # /customer/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
