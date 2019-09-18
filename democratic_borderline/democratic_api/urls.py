from rest_framework import routers

from democratic_api.views import PersonBorderCrossing, LatestPersonCrossedBorder

router = routers.DefaultRouter()
router.register(
    "person_border_crossing", PersonBorderCrossing, base_name="person_border_crossing"
)
router.register(
    "latest_person_crossed_border",
    LatestPersonCrossedBorder,
    base_name="latest_person_crossed_border",
)

urlpatterns = router.urls
