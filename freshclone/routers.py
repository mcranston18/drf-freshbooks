from rest_framework.routers import SimpleRouter

from clients.views import ClientViewSet
from projects.views import ProjectViewSet
from users.views import UserViewSet

router = SimpleRouter()
router.register(r'clients', ClientViewSet, base_name='client')
router.register(r'projects', ProjectViewSet, base_name='project')
router.register(r'users', UserViewSet)
