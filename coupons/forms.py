from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django import forms

from coupons.models import Coupon, Redemption


class CouponRedeemForm(forms.Form):
    """Form for CouponRedeem.

    Be sure to attach the user to .user
    """

    coupon = forms.CharField(label=u'Coupon Code', max_length=40)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CouponRedeemForm, self).__init__(*args, **kwargs)

    def clean_coupon(self):
        code = self.cleaned_data['coupon']
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            raise forms.ValidationError('Sorry, we could not find that coupon code.')
        # Now check to see if the user attached to the form has permission
        # to redeem the coupon.
        if self.user.has_perm('coupons.redeem', coupon):
            return coupon
        else:
            raise forms.ValidationError('Sorry, this coupon code has expired.')

    def save(self):
        coupon = self.cleaned_data['coupon']
        redemption = Redemption(
            user=self.user,
            coupon=coupon,
        )
        redemption.save()
        return redemption
