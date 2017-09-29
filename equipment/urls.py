"""URL pattern definitions for Equipment App"""

from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
    # /equipment/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /equipment/<equipment_id>/
    #url(r'^(?P<equipment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='equipment-detail'),

     # /equipment/add/
    url(r'equipment/add/$', views.EquipmentCreate.as_view(), name='equipment-add'),

    # /equipment/<equipment_id>/tested 
    #url(r'^(?P<equipment_id>[0-9]+)/tested/$', views.tested, name='tested'),
]
