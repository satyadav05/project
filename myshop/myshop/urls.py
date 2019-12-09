"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from garments.views import index,casualshirt,formalshirt,tshirt,search_list,contactus,indianwear,westernwear,footwear,boysclothing,girlsclothing,brand,thankyou,cart
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('',index),
    path('formalshirt',formalshirt),
    path('casualshirt',casualshirt),
    path('tshirt',tshirt),
    path('search_list',search_list),
    path('contactus',contactus),
    path('indianwear',indianwear),
    path('westernwear',westernwear),
    path('footwear',footwear),
    path('boysclothing',boysclothing),
    path('girlsclothing',girlsclothing),
    path('brand',brand),
    path('thankyou',thankyou),
    path('cart<int:x>',cart),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
