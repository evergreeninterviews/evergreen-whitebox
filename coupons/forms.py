from django.core.exceptions import PermissionDenied
from django import forms

from coupons.models import Coupon, Redemption


class CouponRedeemForm(forms.Form):
    """Form for CouponRedeem"""

    coupon = forms.CharField(label=u'Coupon Code', max_length=40)

    def clean_coupon(self):
        code = self.cleaned_data['coupon']
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            raise forms.ValidationError('Sorry, we do not have that coupon code.')
        else:
            return coupon

    def save(self, request):
        coupon = self.cleaned_data['coupon']
        redemption = Redemption(
            user=request.user,
            coupon=coupon,
        )
        try:
            redemption.save()
        except PermissionDenied, permission_error:
            raise forms.ValidationError(str(permission_error))
        else:
            return redemption
