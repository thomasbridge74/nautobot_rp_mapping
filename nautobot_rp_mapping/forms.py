from nautobot.extras.forms import CustomFieldModelForm, CustomFieldFilterForm
from .models import StaticRP, RPGroupEntry
from nautobot.utilities.forms.fields import CommentField, DynamicModelChoiceField
from nautobot.ipam.models import Prefix, IPAddress
from django import forms


class RPForm(CustomFieldModelForm):
    class Meta:
        model = StaticRP
        fields = ("rp_address", "rp_acl_name", "override")


class RPGroupForm(CustomFieldModelForm):
    comments = CommentField()
    mcast_group = DynamicModelChoiceField(queryset=Prefix.objects.all())

    class Meta:
        model = RPGroupEntry
        fields = (
            "group_name",
            "sequence_no",
            "remark",
            "mcast_group",
            "comments",
        )


class StaticRPFilterForm(CustomFieldFilterForm):
    model = StaticRP
    rp_address = forms.ModelChoiceField(
        queryset=IPAddress.objects.all(), required=False
    )
    rp_acl_name = forms.CharField(required=False)
    context = forms.BooleanField(required=False)


class RPGroupEntryFilterForm(CustomFieldFilterForm):
    model = RPGroupEntry
    group_name = forms.ModelChoiceField(queryset=StaticRP.objects.all(), required=False)
    sequence_no = forms.IntegerField(required=False)
    remark = forms.BooleanField(required=False)
    mcast_group = forms.ModelChoiceField(queryset=Prefix.objects.all(), required=False)
    # comments = forms.Textarea(required=False)
