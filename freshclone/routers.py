from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework.routers import SimpleRouter

from clients.views import ClientViewSet, ClientContactsViewSet
from invoices.views import InvoiceViewSet
from projects.views import ProjectViewSet
from users.views import UserViewSet

router = ExtendedSimpleRouter()
(
    router.register(r'clients', ClientViewSet, base_name='client')
          .register(r'contacts',
                    ClientContactsViewSet,
                    base_name='client-contacts',
                    parents_query_lookups=['client'])
)

router.register(r'invoices', InvoiceViewSet, base_name='invoice')
router.register(r'projects', ProjectViewSet, base_name='project')
router.register(r'users', UserViewSet)
