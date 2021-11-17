from rest_framework.routers import DefaultRouter

from .api import ClientViewSet

router = DefaultRouter()

router.register("all", ClientViewSet, basename="user")

urlpatterns = router.urls
