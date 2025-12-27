from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("blog/", include("blog.urls")),
    path("", include("infopages.urls")),
    path("", include("core.urls")),
]
# ---- STATIC/MEDIA ----
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Adminita Demo Site"
admin.site.site_title = "Adminita Demo Site"
admin.site.index_title = "Welcome to Adminita Demo Site"
