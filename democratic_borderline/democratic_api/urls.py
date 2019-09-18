from rest_framework import routers

from democratic_api.views import PersonBorderCrossing

router = routers.DefaultRouter()
router.register(
    "person_border_crossing", PersonBorderCrossing, base_name="person_border_crossing"
)

urlpatterns = router.urls
