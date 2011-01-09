from django.contrib import admin

from coupons.models import Coupon


class CouponAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coupon, CouponAdmin)
