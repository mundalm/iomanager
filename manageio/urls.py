"""URL pattern definitions for Equipment App"""

from django.conf.urls import url
from . import views

app_name = 'manageio'

urlpatterns = [
    # /manageio/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /equipment/<equipment_id>/
    #url(r'^(?P<equipment_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='equipment-detail'),
    url(r'equipment/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='equipment-detail'),

     # /equipment/add/
    url(r'equipment/add/$', views.EquipmentCreate.as_view(), name='equipment-add'),

    # /equipment/2/edit
    url(r'equipment/(?P<pk>[0-9]+)/edit/$', views.EquipmentUpdate.as_view(), name='equipment-update'),

     # /equipment/2/delete
    url(r'equipment/(?P<pk>[0-9]+)/delete/$', views.EquipmentDelete.as_view(), name='equipment-delete')
]
