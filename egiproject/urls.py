from django.conf import settings
from django.conf.urls.defaults import *

from staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(regex=  r'^admin/doc/',
        view=   include('django.contrib.admindocs.urls'),
    ),
    url(regex=  r'^admin/',
        view=   include(admin.site.urls),
    ),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
