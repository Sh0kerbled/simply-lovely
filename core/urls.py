from django.contrib import admin
from django.urls import path
from app.views import main_page
from users.views import auth_page, join_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('auth/', auth_page, name='auth'),
    path('join/', join_page, name='join'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
