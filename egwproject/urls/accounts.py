from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(name=   'accounts_login',
        regex=  r'login/$',
        view=   'django.contrib.auth.views.login',
    ),
    url(name=   'accounts_logout',
        regex=  r'logout/$',
        view=   'django.contrib.auth.views.logout',
        kwargs= dict(
            next_page='/',
        ),
    ),
)
