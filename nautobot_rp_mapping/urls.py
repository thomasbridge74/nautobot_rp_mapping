from django.urls import path
from . import views, models
# from nautobot.views.generic import ObjectChangeLogView

urlpatterns = (
    # Entries for the RP itself
    path("rp/", views.RPListView.as_view(), name="staticrp_list"),
    path("rp/add/", views.RPEditView.as_view(), name="staticrp_add"),
    path("rp/<uuid:pk>/", views.RPView.as_view(), name="staticrp"),
    path("rp/<uuid:pk>/edit/", views.RPEditView.as_view(), name="staticrp_edit"),
    path("rp/<uuid:pk>/delete/", views.RPDeleteView.as_view(), name="staticrp_delete"),
    # path(
    #     "rp/<uuid:pk>/changelog/",
    #     ObjectChangeLogView.as_view(),
    #     name="staticrp_changelog",
    #     kwargs={"model": models.StaticRP},
    # ),
    # Entries for the groups belonging to the RP.
    path("rpgroup/", views.RPGroupListView.as_view(), name="rpgroupentry_list"),
    path("rpgroup/add/", views.RPGroupEditView.as_view(), name="rpgroupentry_add"),
    path("rpgroup/<uuid:pk>/", views.RPGroupView.as_view(), name="rpgroupentry"),
    path(
        "rpgroup/<uuid:pk>/edit",
        views.RPGroupEditView.as_view(),
        name="rpgroupentry_edit",
    ),
    path(
        "rpgroup/<uuid:pk>/delete",
        views.RPGroupDeleteView.as_view(),
        name="rpgroupentry_delete",
    ),
    # path(
    #     "rpgroup/<uuid:pk>/changelog",
    #     ObjectChangeLogView.as_view(),
    #     name="rpgroupentry_changelog",
    #     kwargs={"model": models.RPGroupEntry},
    # ),
)
