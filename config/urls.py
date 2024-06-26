from pybo.views import base_views
# 2024-03-13 추가
from django.contrib import admin
from django.urls import include, path
from pybo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]
