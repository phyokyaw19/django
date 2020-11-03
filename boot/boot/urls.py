from django.urls import include, path
from django.contrib import admin
#from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('check.urls')),
    path('accounts/', include('accounts.urls')),
    path('machines/', include('machine.urls')),
    path('documents/', include('documents.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
