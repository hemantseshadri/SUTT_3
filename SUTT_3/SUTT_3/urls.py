"""SUTT_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('inventory/',views.index,name="inventory"),
    #path('inventory/cart/',views.cart,name="cart"),
    path('inventory/<int:Item_id>/',views.detail,name='detail'),
    #path('inventory/cart/checkout/',views.checkoutview,name="checkout"),
    #path('inventory/cart/<int:Issue_Item_id>',views.removefromcart,name="removefromcart"),
    path('profile/',views.profile,name="profile"),
    path('signup/',views.signup,name="modsignup"),
    path('moderatorview/',views.moderatorview,name="moderatorview"),
    path('additems/',views.additems,name="additems"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('moderatorview/<int:item_id>/edit',views.editinventory,name="edit"),
    path('upload/',views.upload,name="upload"),
    path('profile/<int:Return_item_id>',views.returndetail,name='returndetail'),
    # path('profile/<int:final_issued_item_id>/',views.returnitem,name="returnitem"),
    path('export/',views.export_excel,name="export")

]
