from netbox.views import generic
# from extras.models.objectchange import ObjectChange
from django.shortcuts import get_object_or_404
from . import forms, models, tables

class DNSListView(generic.ObjectListView):
    queryset = models.DNS.objects.all()
    table = tables.DNSTable

class DNSView(generic.ObjectView):
    queryset = models.DNS.objects.all()

class DNSEditView(generic.ObjectEditView):
    queryset = models.DNS.objects.all()
    form = forms.DNSForm

class DNSDeleteView(generic.ObjectDeleteView):
    queryset = models.DNS.objects.all()

class IPv4RoutesListView(generic.ObjectListView):
    queryset = models.IPv4Routes.objects.all()
    table = tables.IPv4RoutesTable

class IPv4RoutesView(generic.ObjectView):
    queryset = models.IPv4Routes.objects.all()

class IPv4RoutesChangeLogView(generic.ObjectChangeLogView):
    queryset =None

    # def get(self, request, pk):
    #     instance = get_object_or_404(models.IPv4Routes, pk=pk)
    #     self.queryset = self.queryset.filter(
    #         object_id=pk,
    #         changed_object_type=instance.get_ct()
    #     )
    #     return super().get(request)

class IPv4RoutesEditView(generic.ObjectEditView):
    queryset = models.IPv4Routes.objects.all()
    form = forms.IPv4RoutesForm

    def get_object(self,*args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return get_object_or_404(models.IPv4Routes, pk=pk)
        return None

class IPv4RoutesDeleteView(generic.ObjectDeleteView):
    queryset = models.IPv4Routes.objects.all()

class IPv6RoutesListView(generic.ObjectListView):
    queryset = models.IPv6Routes.objects.all()
    table = tables.IPv6RoutesTable

class IPv6RoutesView(generic.ObjectView):
    queryset = models.IPv6Routes.objects.all()

class IPv6RoutesEditView(generic.ObjectEditView):
    queryset = models.IPv6Routes.objects.all()
    form = forms.IPv6RoutesForm

class IPv6RoutesDeleteView(generic.ObjectDeleteView):
    queryset = models.IPv6Routes.objects.all()

class IPSecProfileListView(generic.ObjectListView):
    queryset = models.VPNaaSIPSecProfile.objects.all()
    table = tables.IPSecProfileTable

class IPSecProfileView(generic.ObjectView):
    queryset = models.VPNaaSIPSecProfile.objects.all()

class IPSecProfileEditView(generic.ObjectEditView):
    queryset = models.VPNaaSIPSecProfile.objects.all()
    form = forms.IPSecProfileForm

class IPSecProfileDeleteView(generic.ObjectDeleteView):
    queryset = models.VPNaaSIPSecProfile.objects.all()

class TLSProfileListView(generic.ObjectListView):
    queryset = models.TLSProfile.objects.all()
    table = tables.TLSProfileTable

class TLSProfileView(generic.ObjectView):
    queryset = models.TLSProfile.objects.all()

class TLSProfileEditView(generic.ObjectEditView):
    queryset = models.TLSProfile.objects.all()
    form = forms.TLSProfileForm

class TLSProfileDeleteView(generic.ObjectDeleteView):
    queryset = models.TLSProfile.objects.all()

class TerminationListView(generic.ObjectListView):
    queryset = models.Termination.objects.all()
    table = tables.TerminationTable

class TerminationView(generic.ObjectView):
    queryset = models.Termination.objects.all()

class TerminationEditView(generic.ObjectEditView):
    queryset = models.Termination.objects.all()
    form = forms.TerminationForm

class TerminationDeleteView(generic.ObjectDeleteView):
    queryset = models.Termination.objects.all()

class RemoteAccessTunnelListView(generic.ObjectListView):
    queryset = models.RemoteAccessTunnel.objects.all()
    table = tables.RemoteAccessTunnelTable

class RemoteAccessTunnelView(generic.ObjectView):
    queryset = models.RemoteAccessTunnel.objects.all()

class RemoteAccessTunnelEditView(generic.ObjectEditView):
    queryset = models.RemoteAccessTunnel.objects.all()
    form = forms.RemoteAccessTunnelForm

class RemoteAccessTunnelDeleteView(generic.ObjectDeleteView):
    queryset = models.RemoteAccessTunnel.objects.all()