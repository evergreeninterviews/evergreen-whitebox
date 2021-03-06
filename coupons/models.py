import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from coupons.exceptions import Expired, RedemptionLimitExceeded


class Coupon(models.Model):
    """A coupon code that can be redeemed."""

    code = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    max_redemptions = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, auto_now_add=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        permissions = (
            ('redeem', 'Redeem a coupon.'),
        )

    def __unicode__(self):
        return self.code

    def num_redemptions(self):
        return self.redemptions.count()


class Redemption(models.Model):
    """The redemption of a coupon by another object"""

    user = models.ForeignKey(User, related_name='coupon_redemptions')
    coupon = models.ForeignKey(Coupon, related_name='redemptions')
    created = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        pass

    def __unicode__(self):
        return u"{0} redeemed {1}".format(self.user, self.coupon)

    def get_absolute_url(self):
        return reverse('coupons_redemption_detail', kwargs=dict(object_id=self.id))
