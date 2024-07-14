from django.contrib import admin
from django.urls import path, include
import main_app.urls as main_app_urls
import oge.urls as oge_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_app_urls)),
    path('oge/', include(oge_urls)),
]
