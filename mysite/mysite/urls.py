from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('sample/', include('sample.urls')),
    path('admin/', admin.site.urls),
]
