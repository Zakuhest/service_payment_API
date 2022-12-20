from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payment', api.PaymentUserViewSet, 'pay_v2')
router.register(r'service', api.ServicesViewSet, 'service_v2')
router.register(r'expired', api.ExpiredPaymentsViewSet, 'exp_v2')

api_urlpatterns = router.urls