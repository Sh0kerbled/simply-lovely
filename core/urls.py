from django.contrib import admin
from django.urls import path, include
from app.views import main_page
from users.views import auth_page, join_page
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
