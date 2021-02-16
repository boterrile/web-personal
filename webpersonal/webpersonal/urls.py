"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

#En DES(desarollo) no sirve los ficheros media. Para poder ver los ficheros media en DES tenemos que tener el DEBUG activo
#  y añadiendo una configuracion extendida a Django para acceder a las variabes MEDIA_ROOT  y MEDIA_URL en settings.py
from django.conf import settings 


urlpatterns = [
    path('',core_views.home, name='home'),
    path('about-me/',core_views.about, name='about'),
    path('portfolio/',portfolio_views.portfolio, name='portfolio'),
    path('contact/',core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

# Para acceder a los media en DESARROLLO: Si La variable DEBUG esta TRUE (en DE S)
if settings.DEBUG:
    from django.conf.urls.static import static #permite servir ficheros estaticos

    # tenemos que decirle a los urlpatterns que les sirva los ficheros solicitados. Busca en MEDIA_ROOT y los sirve en MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 