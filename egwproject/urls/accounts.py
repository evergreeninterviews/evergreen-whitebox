from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(regex=  r'logout/$',
        view=   'django.contrib.auth.views.logout',
        kwargs= dict(
            next_page='/',
        ),
    ),
)
