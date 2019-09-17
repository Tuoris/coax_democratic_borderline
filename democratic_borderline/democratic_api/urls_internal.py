from rest_framework import routers

from democratic_api.views_internal import (
    BorderCrossingViewSet,
    ForbiddenStuffViewSet,
    NationalityViewSet,
    PersonViewSet,
)

router = routers.DefaultRouter()
router.register("border_crossing", BorderCrossingViewSet)
router.register("forbidden_stuff", ForbiddenStuffViewSet)
router.register("nationality", NationalityViewSet)
router.register("people", PersonViewSet)

urlpatterns = router.urls
