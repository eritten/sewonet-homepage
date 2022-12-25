from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap # new
from home.sitemap import HomeSitemap
from blog.sitemap import BlogSitemap
from django.conf.urls.static import static
from django.conf import settings
maps = {"blog": BlogSitemap, "home": HomeSitemap}

urlpatterns = [
path('/language/', include('django.conf.urls.i18n')),
path('admin/', admin.site.urls),
path('blog/', include('blog.urls')),
    path('sitemap.xml', sitemap, # new
        {'sitemaps': maps},
        name='django.contrib.sitemaps.views.sitemap'),
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('privacy/', views.privacy, name='privacy'),
path('services/', views.services, name='services'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)