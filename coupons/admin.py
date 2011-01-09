from django.contrib import admin

from coupons.models import Coupon


class CouponAdmin(admin.ModelAdmin):

    list_display = ('code', 'num_redemptions', 'expires', 'num_redemptions')


admin.site.register(Coupon, CouponAdmin)
