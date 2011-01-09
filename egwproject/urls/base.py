from django.conf import settings
from django.conf.urls.defaults import *

from staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(regex=  r'^accounts/',
        view=   include('egwproject.urls.accounts'),
    ),
    url(regex=  r'^admin/doc/',
        view=   include('django.contrib.admindocs.urls'),
    ),
    url(regex=  r'^admin/',
        view=   include(admin.site.urls),
    ),
    url(regex=  r'^convert/',
        view=   include('lazysignup.urls'),
    ),
    url(regex=  r'^coupons/',
        view=   include('coupons.urls'),
        kwargs= dict(
            allow_lazy_user=True,
        ),
    ),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
