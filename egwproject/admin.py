from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from coupons.models import Redemption


class RedemptionInline(admin.TabularInline):

    model = Redemption
    extra = 1
    fields = ('coupon', 'created')
    readonly_fields = ('created',)


class ExtendedUserAdmin(UserAdmin):

    inlines = (
        RedemptionInline,
    )


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
