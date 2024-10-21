from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', include('apps.about_us.urls')),
    path('contact_us/', include('apps.contact_us.urls')),
    path('', include('apps.landing_page.urls')),
    path('news_page/', include('apps.news_page.urls')),
    path('user/', include('apps.user.urls')),
    path('buscar/', include('apps.search.urls')),  
]
