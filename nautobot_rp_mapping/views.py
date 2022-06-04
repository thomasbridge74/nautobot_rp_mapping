from nautobot.extras.views import generic
from . import forms, models, tables, filtersets


class RPView(generic.ObjectView):
    queryset = models.StaticRP.objects.all()
    template_name = "nautobot_rp_mapping/staticrp.html"

    # def get_extra_context(self, request, instance):
    #     table = tables.GroupTable(instance.mcast_rp.all())
    #     # table.configure(request)
    #     return {"rules_table": table}


class RPListView(generic.ObjectListView):
    queryset = models.StaticRP.objects.all()
    table = tables.RPTable
    action_buttons = ()
    # filterset = filtersets.StaticRPFilterSet
    # filterset_form = forms.StaticRPFilterForm
    template_name = "nautobot_rp_mapping/staticrp_list.html"

class RPEditView(generic.ObjectEditView):
    queryset = models.StaticRP.objects.all()
    model_form = forms.RPForm


class RPDeleteView(generic.ObjectDeleteView):
    queryset = models.StaticRP.objects.all()


class RPGroupView(generic.ObjectView):
    queryset = models.RPGroupEntry.objects.all()


class RPGroupListView(generic.ObjectListView):
    queryset = models.RPGroupEntry.objects.all()
    table = tables.GroupTable
    filterset = filtersets.RPGroupEntryFilterSet
    filterset_form = forms.RPGroupEntryFilterForm


class RPGroupEditView(generic.ObjectEditView):
    queryset = models.RPGroupEntry.objects.all()
    form = forms.RPGroupForm


class RPGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.RPGroupEntry.objects.all()
