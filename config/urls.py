from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skeditor/', include('ckeditor_uploader.urls')),
    path('', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('events/', include('events.urls')),
    path('note/', include('note.urls')),
    path('pwd/', include('pwd.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
