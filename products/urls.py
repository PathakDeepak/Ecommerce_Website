

from django.urls import path
from django.conf.urls import url


from .views import (
    ProductListView,
    product_list_view,
    product_detail_view,
    ProductDetailView,
    ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='details'),


    #path('products-fbv', product_list_view),
    # path('(?P<pk>\d+)', ProductDetailView.as_view()),
    # path('(?P<pk>\d+)', product_detail_view),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^(?P<pk>\d+)/$', product_detail_view),
    ]
