from django.db import models
from nautobot.core.models.generics import PrimaryModel
from nautobot.ipam.models import IPAddress, Prefix
from nautobot.dcim.models import Site, Region
from nautobot.extras.utils import extras_features
from django.urls import reverse


@extras_features("custom_fields", "relationships")
class StaticRP(PrimaryModel):
    rp_address = models.ForeignKey(
        to=IPAddress, on_delete=models.DO_NOTHING, related_name="ip_address"
    )
    rp_acl_name = models.CharField(max_length=64, blank=False, unique=True)
    override = models.BooleanField(default=True)
    site = models.ForeignKey(
        to=Site, on_delete=models.DO_NOTHING,
        null=True
    )
    region = models.ForeignKey(
        to=Region, on_delete=models.DO_NOTHING, null=True
    )

    class Meta:
        ordering = ("rp_address",)
        verbose_name_plural = "Static RPs"

    def __str__(self):
        return str(self.rp_address).split("/")[0]

    def get_absolute_url(self):
        return reverse("plugins:nautobot_rp_mapping:staticrp", args=[self.pk])


@extras_features("custom_fields", "relationships")
class RPGroupEntry(PrimaryModel):
    group_name = models.ForeignKey(
        to=StaticRP, on_delete=models.CASCADE, related_name="mcast_rp"
    )
    sequence_no = models.PositiveBigIntegerField()
    remark = models.BooleanField()
    comments = models.CharField(max_length=128)
    mcast_group = models.ForeignKey(
        to=Prefix, on_delete=models.DO_NOTHING, related_name="mcast_groups", null=True
    )

    class Meta:
        ordering = (
            "group_name",
            "sequence_no",
        )
        verbose_name_plural = "RP Group Entries"

    def __str__(self):
        if self.remark:
            return f"{self.sequence_no} remark {self.comments}"
        elif "/32" in str(self.mcast_group):
            host = str(self.mcast_group).replace("/32", "")
            return f"{self.sequence_no} permit host {host}"
        else:
            return f"{self.sequence_no} permit {str(self.mcast_group)}"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_rp_mapping:rpgroupentry", args=[self.pk])
