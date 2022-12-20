from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payment', api.PaymentUserViewSet, 'pay_v1')

api_urlpatterns = router.urls