from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #account
    path('api/account/', include("account.urls")),

    #password recovery
    path('api/recovery-account/', include("recovery_account.urls")),

    #contact
    path('api/contact/', include("contact.urls")),

    #main
    path('api/main/', include("main.urls")),

    #blog
    path('api/blog/', include("blog.urls")),

    #payment
    path('api/payment_method/', include("payment_method.urls")),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
