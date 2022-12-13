from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("v1/app/", include("app.urls")),
    path("secret-admin/", admin.site.urls),
]

admin.site.index_title = "PersianText"
admin.site.site_title = "PersianText Django Admin"
admin.site.site_header = "PersianText Django Administration Panel"
