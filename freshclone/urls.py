from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Freshclone API')
admin.autodiscover()

from freshclone.routers import router

BASE_API_URL = 'api/v1'

api_urls = [
    url(
        r'^o/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('', include(router.urls)),
    url(r'^docs/', schema_view)
]

urlpatterns = [
    url(r'^api/v1/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
]
