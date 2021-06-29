"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v

#from django.conf import settings
#from django.conf.urls.static import static

#For translate:
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path(_('admin/'), admin.site.urls),
    path('', include('blogapp.urls')),

    path('register/', v.register, name='register'),
    path('profile_update/', v.profile_update, name='profile_update'),
    path('', include("django.contrib.auth.urls")),
    path('password/', v.change_password, name='change_password'),
#    path('email/', v.change_email, name='change_email'),
    path('afterlogin', v.afterlogin, name='afterlogin'),
    path('afterlogout', v.afterlogout, name='afterlogout'),

    path('ckeditor', include("ckeditor_uploader.urls")),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""path('', include("django.contrib.auth.urls")) is handling login & logout urls"""