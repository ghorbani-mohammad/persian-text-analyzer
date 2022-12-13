from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("v1/app/", include("app.urls")),
    path("secret-admin/", admin.site.urls),
]

admin.site.index_title = "Persian Text"
admin.site.site_title = "Persian Text Django Admin"
admin.site.site_header = "Persian Text Django Administration Panel"
