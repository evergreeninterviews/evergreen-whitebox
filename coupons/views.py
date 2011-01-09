from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.list_detail import object_detail, object_list
from django.views.generic.simple import direct_to_template

from coupons.forms import CouponRedeemForm
from coupons.models import Redemption


@login_required
def redeem(request, template="coupons/redeem.html", extra_context=None, *args, **kwargs):
    extra_context = extra_context or {}
    if request.method == 'POST':
        form = CouponRedeemForm(request.POST, user=request.user)
        if form.is_valid():
            redemption = form.save()
            return redirect(redemption)
    else:
        form = CouponRedeemForm(initial=request.GET, user=request.user)
    extra_context.update(
        form=form,
    )
    return direct_to_template(
        request,
        template=template,
        extra_context=extra_context,
        *args, **kwargs
    )


@login_required
def redemption_list(request, *args, **kwargs):
    queryset = Redemption.objects.filter(user=request.user)
    return object_list(request, queryset=queryset, *args, **kwargs)


@login_required
def redemption_detail(request, *args, **kwargs):
    queryset = Redemption.objects.filter(user=request.user)
    return object_detail(request, queryset=queryset, *args, **kwargs)
