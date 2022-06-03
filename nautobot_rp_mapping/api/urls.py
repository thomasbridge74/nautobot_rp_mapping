from rest_framework import routers
from . import views

app_name = "nautobot_rp_mapping"

router = routers.DefaultRouter()
router.register("rp", views.StaticRPViewSet)
router.register("rpgroup", views.RPGroupEntryViewSet)

urlpatterns = router.urls
