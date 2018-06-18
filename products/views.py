from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


from carts.models import Cart
from .models import Product


# Create your views here.

#class based Listviews
class ProductListView(ListView):
    queryset = Product.objects.all()
    print(queryset)


#function based Listview
def product_list_view(request):
    queryset = Product.objects.all()
    title = "Product"
    context = {
        'title': title,
        'object_list': queryset,
    }
    return render(request, 'products/product_list.html', context)

#class based Detailviews
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all()



#function based Detailview
def product_detail_view(request, pk=None, *args, **kwargs):
    print(args)
    print(kwargs)
    #instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)

    title = "Product"
    context = {
        'title': title,
        'brand_name': instance.title,
        'object': instance,
    }
    return render(request, 'products/product_detail.html', context)
