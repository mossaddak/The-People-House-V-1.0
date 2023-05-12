from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #account
    path('api/account/', include('account.urls')),

    #password recovery
    path('api/recovery-account/', include("recovery_account.urls")),

    #contact
    path('api/contact/', include("contact.urls")),

    #main
    path('api/main/', include("main.urls"))
]
