from netbox.api.routers import NetBoxRouter
from . import views

app_name = "nautobot_rp_mapping"

router = NetBoxRouter()
router.register("rp", views.StaticRPViewSet)
router.register("rpgroup", views.RPGroupEntryViewSet)

urlpatterns = router.urls
