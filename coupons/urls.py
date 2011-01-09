from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to


urlpatterns = patterns('coupons.views',
    url(name=   'coupons',
        regex=  r'^$',
        view=   'index',
    ),
    url(name=   'coupons_redeem',
        regex=  r'^redeem/$',
        view=   'redeem',
    ),
    url(name=   'coupons_redemption_list',
        regex=  r'^redeemed/$',
        view=   'redemption_list',
    ),
    url(name=   'coupons_redemption_detail',
        regex=  r'^redeemed/(?P<object_id>\d+)/$',
        view=   'redemption_detail',
    ),
)
