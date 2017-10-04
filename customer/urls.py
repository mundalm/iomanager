"""URL pattern definitions for Equipment App"""

from django.conf.urls import url
from . import views

app_name = 'customer'

urlpatterns = [
    # /customer/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /customer/<customer_id>/
    url(r'customer/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='customer-detail'),

     # /customer/add/
    url(r'add/$', views.CustomerCreate.as_view(), name='customer-add'),

    # /customer/2/edit
    url(r'(?P<pk>[0-9]+)/edit/$', views.CustomerUpdate.as_view(), name='customer-update'),

     # /customer/2/delete
    url(r'(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer-delete')
]
