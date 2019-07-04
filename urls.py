"""quickshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shop1.views import activate,signup,index,user_login,user_logout,single,phonepage,Search,add_cart,user_cart,Removefromcart,quantity,Phonesproduct,returnhome
from shop1 import views
from shop1.views import payment ,checkout
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$',index),
    url(r'^Signup$',signup),
    url(r'^login$',user_login),
    url(r'^returnhome$',returnhome),
    url(r'^search$',Search),
    url(r'^cart$',user_cart),
    url(r'^checkout-(?P<checkid>[0-9A-Za-z_\-]+)$', checkout),
    url(r'^id-pay$',payment),
   
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        views.activate, name='activate'),
    url(r'^logout$',user_logout),
    url(r'^phones-(?P<brandname>[0-9A-Za-z_\-]+)$',Phonesproduct),

    url(r'^account/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^account/password_reset_done$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^account/reset_(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^account/reset_done$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^cart/(?P<item>[0-9A-Za-z_\-]+)$',add_cart),
    url(r'^removefromcart/(?P<modelid>[0-9A-Za-z_\-]+)$',Removefromcart),
    url(r'^quantity/(?P<quantityid>[0-9A-Za-z_\-]+)$',quantity),
    url(r'^(?P<id>[0-9A-Za-z_\-]+)$',views.single,name='single'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
