from django.contrib.auth.models import User
from django.test import TestCase

from coupons.models import Coupon, Redemption


def saved(model, *args, **kwargs):
    obj = model(*args, **kwargs)
    obj.save()
    return obj


class TestCoupons(TestCase):

    def test_redemption_limits(self):
        user = saved(User, username='user')
        coupon = saved(Coupon, code='coupon', max_redemptions=3)
        redemption1 = saved(Redemption, user=user, coupon=coupon)
        redemption2 = saved(Redemption, user=user, coupon=coupon)
        assert user.has_perm('coupons.redeem', coupon)
        redemption3 = saved(Redemption, user=user, coupon=coupon)
        assert not user.has_perm('coupons.redeem', coupon)
