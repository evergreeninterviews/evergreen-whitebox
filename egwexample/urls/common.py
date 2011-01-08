from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(regex=  '',
        view=   include('egwproject.urls.common'),
    ),
)
