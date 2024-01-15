from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from core.utils import is_superuser_or_staff
from crud.views import (IndexView, UserListView, ProductListView, CategoryListView,
                        UserCreate, UserUpdate, UserDelete,
                        ProductCreate, ProductUpdate, ProductDelete,
                        CategoryCreate, CategoryUpdate, CategoryDelete)


app_name = 'crud'

urlpatterns = [
    path('index/', user_passes_test(is_superuser_or_staff)(
        IndexView.as_view()), name='admin_panel'),

    path('users/', user_passes_test(is_superuser_or_staff)(
        UserListView.as_view()), name='user_list'),
    path('users/add/', user_passes_test(is_superuser_or_staff)(
        UserCreate.as_view()), name='user_add'),
    path('user/update/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        UserUpdate.as_view()), name='user_update'),
    path('user/delete/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        UserDelete.as_view()), name='user_delete'),

    path('products/', user_passes_test(is_superuser_or_staff)(
        ProductListView.as_view()), name='product_list'),
    path('products/add/', user_passes_test(is_superuser_or_staff)(
        ProductCreate.as_view()), name='product_add'),
    path('products/update/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        ProductUpdate.as_view()), name='product_update'),
    path('products/delete/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        ProductDelete.as_view()), name='product_delete'),

    path('categories/', user_passes_test(is_superuser_or_staff)(
        CategoryListView.as_view()), name='category_list'),
    path('category/add/', user_passes_test(is_superuser_or_staff)(
        CategoryCreate.as_view()), name='category_add'),
    path('category/update/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        CategoryUpdate.as_view()), name='category_update'),
    path('category/delete/<int:pk>/', user_passes_test(is_superuser_or_staff)(
        CategoryDelete.as_view()), name='category_delete'),
]
