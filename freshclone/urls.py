from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from freshclone.routers import router

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
]
