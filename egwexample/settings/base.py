from egwproject.settings.base import *


ROOT_URLCONF = 'egwexample.urls.base'

AUTHENTICATION_BACKENDS += (
    'coupons.backends.DefaultCouponRedemptionBackend',
)
