import datetime

from coupons.models import Coupon


class DefaultCouponRedemptionBackend(object):
    """Provides default authorization rules for coupon redemption."""

    supports_object_permissions = True
    supports_anonymous_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user, perm, obj=None):
        if perm == 'coupons.redeem':
            if isinstance(obj, Coupon):
                # Users cannot redeem coupons that have expired.
                if obj.expires and datetime.datetime.now() >= obj.expires:
                    return False
                # Users cannot redeem limited-redemption coupons after max times.
                if obj.max_redemptions and obj.num_redemptions() >= obj.max_redemptions:
                    return False
                # Otherwise, allow authenticated users to redeem.
                if user.is_authenticated():
                    return True
            else:
                # No coupon given.
                # Authenticated users can attempt to redeem coupons.
                return user.is_authenticated()
