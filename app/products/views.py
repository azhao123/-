from django.shortcuts import render
from django.views.generic import View
from .models import Product


class CategoryListView(View):
    def get(self, request, id):
        categorys = Product.objects.filter(tag=int(id))
        type = request.GET.get('type', "")
        if type:
            if type == 'sell':
                categorys = categorys.order_by("ku_cun")
            elif type == 'price':
                categorys = categorys.order_by("price")
            elif type == 'comment':
                categorys = categorys.order_by("comment")


        return render(request, "category_list.html", {
            "categorys":categorys,
            "type":type
        })


class CategoryView(View):
    def get(self, request):
        return render(request, "category.html")

class ProductionView(View):
    def get(self, request, p_id):
        production = Product.objects.get(id=int(p_id))
        return render(request, "views.html", {
            "production": production
        })


