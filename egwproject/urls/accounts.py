from django.conf.urls.defaults import *

from egwproject.forms import UserCreationFormWithEmail


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
    url(name=   'lazysignup_convert',
        regex=  r'^convert/$',
        view=   'lazysignup.views.convert',
        kwargs= dict(
            form_class=UserCreationFormWithEmail,
        ),
    ),
)
