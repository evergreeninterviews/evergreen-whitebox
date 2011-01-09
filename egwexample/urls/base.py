from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(regex=  u'',
        view=   include('egwproject.urls.base'),
    ),
)
