from django.contrib import admin
from django.urls import include,path

# for showing media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), #put all app urls here
    path('listings/', include('listings.urls')), #put all app urls here
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #to show up uploaded media
