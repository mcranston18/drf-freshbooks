from rest_framework.routers import SimpleRouter

from clients.views import ClientViewSet

router = SimpleRouter()
router.register(r'clients', ClientViewSet, base_name='client')
