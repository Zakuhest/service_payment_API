from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.GetUsersView, basename="users")

urlpatterns = router.urls