# -*_ coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from products.models import Product


class IndexView(View):
    def get(self, request):
        firsts = Product.objects.filter(tag=1)[:4]
        seconds = Product.objects.filter(tag=2)[:4]
        thirds = Product.objects.filter(tag=3)[:4]

        return render(request, "index.html",{
            'firsts': firsts,
            'seconds': seconds,
            'thirds': thirds
        })


class HomeView(View):
    def get(self, request):
        return render(request, "userhome.html")

class ShopCartView(View):
    def get(self, request):
        return render(request, 'shopcart.html')

class TesttView(View):
    def get(self, request):
        t = Product.objects.all()
        return render(request, "test.html", {
            "t": t
        })
