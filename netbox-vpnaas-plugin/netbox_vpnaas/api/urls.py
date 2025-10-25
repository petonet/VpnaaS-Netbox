from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_vpnaas'

router = NetBoxRouter()
router.register('dns', views.DNSViewSet)
router.register('ipv4routes', views.IPv4RoutesViewSet)
router.register('ipv6routes', views.IPv6RoutesViewSet)
router.register('ipsecprofile', views.IPSecProfileViewSet)
router.register('tlsprofile', views.TLSProfileViewSet)
router.register('termination', views.TerminationViewSet)
router.register('remoteaccesstunnel', views.RemoteAccessTunnelViewSet)

urlpatterns = router.urls