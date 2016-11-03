from django.conf.urls import url, include
from django.contrib import admin

from freshclone.routers import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]
