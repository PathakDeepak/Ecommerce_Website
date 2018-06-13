from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

# Create your views here.

# class SearchProductView(ListView, request):
#     query = request.GET.get('q')
#     queryset = Product.objects.filter(title__iexact='hats')

#function based Listview
def search_product_view(request):
    query = request.GET.get('q')
    if query is not None:
        queryset = Product.objects.filter(title__icontains=query)
    else:
        queryset = Product.objects.none()
    context = {
        'object_list': queryset,
    }
    return render(request, 'search/search_view.html', context)