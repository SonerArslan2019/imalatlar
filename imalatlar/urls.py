import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("imalatlar.apps.home.urls", namespace='home')),
    path('sld/', include("imalatlar.apps.sld.urls", namespace='sld')),
    path('mr30/', include("imalatlar.apps.mr30.urls", namespace='mr30')),
    path('user/', include("imalatlar.apps.user.urls", namespace='user')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
