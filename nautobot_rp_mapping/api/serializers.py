from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from ..models import RPGroupEntry, StaticRP
from nautobot.ipam.api.serializers import NestedPrefixSerializer


class StaticRPSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_rp_mapping-api:staticrp-detail"
    )

    class Meta:
        model = StaticRP
        fields = (
            "id",
            "url",
            "display",
            "rp_address",
            "rp_acl_name",
            "override",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class RPGroupEntrySerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_rp_mapping-api:rpgroupentry-detail"
    )
    mcast_group = NestedPrefixSerializer()

    class Meta:
        model = RPGroupEntry
        fields = (
            "id",
            "url",
            "group_name",
            "sequence_no",
            "remark",
            "comments",
            "mcast_group",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
