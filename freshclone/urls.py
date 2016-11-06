from django.conf.urls import url, include
from django.contrib import admin

from freshclone.routers import router

urlpatterns = [
    url(r'^api/v1/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
