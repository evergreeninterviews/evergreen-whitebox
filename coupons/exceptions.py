from django.core.exceptions import PermissionDenied


class Expired(PermissionDenied):
    pass


class RedemptionLimitExceeded(PermissionDenied):
    pass
