from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manageio/', include('manageio.urls')),
    url(r'^customer/', include('customer.urls')),
]
