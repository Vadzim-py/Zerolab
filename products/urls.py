from django.urls import path
from products.views import products, bookmark_add, bookmark_delete, product_review

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('review/<int:product_id>/', product_review, name='product_review'),
    path('category/<int:category_id>/', products, name='category'),
    path('baskets/add/<int:product_id>/', bookmark_add, name='bookmark_add'),
    path('baskets/remove/<int:bookmark_id>/', bookmark_delete, name='bookmark_delete'),
]
