from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.static import serve
from core.yasg import urlpatterns_yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns_yasg)),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('api/v1/testapp/', include("apps.testapp.urls"))
]


if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]