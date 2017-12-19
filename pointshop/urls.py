"""pointshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from pointshop.settings import MEDIA_ROOT
from users.views import HomeView, ShopCartView, IndexView, TesttView
from products.views import CategoryListView, CategoryView, ProductionView




urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^$', IndexView.as_view(), name="index" ),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^home/$',HomeView.as_view(), name="home"),
    url(r'^category/list/(?P<id>\d+)$', CategoryListView.as_view(), name= "category_list"),
    url(r'^category/$', CategoryView.as_view(), name= "category"),
    url(r'^shopcart/$', ShopCartView.as_view(), name= "shopcart"),
    url(r'^production/(?P<p_id>\d+)$', ProductionView.as_view(), name="productions"),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^test/$', TesttView.as_view(), name="test")

]
