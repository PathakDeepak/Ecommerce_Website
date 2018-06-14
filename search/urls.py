from django.urls import path
from django.conf.urls import url

from .views import search_product_view

app_name= 'search_url'
urlpatterns = [
      path('', search_product_view, name='query'),
      ]