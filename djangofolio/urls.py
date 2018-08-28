from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.home, name='home'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
