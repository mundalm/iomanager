"""URL pattern definitions for Equipment App"""

from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
    # /equipment/
    url(r'^$', views.index, name='index'),

    # /equipment/<equipment_id>/
    url(r'^(?P<equipment_id>[0-9]+)/$', views.detail, name='detail'),

    # /equipment/<equipment_id>/tested 
    url(r'^(?P<equipment_id>[0-9]+)/tested/$', views.tested, name='tested'),
]
