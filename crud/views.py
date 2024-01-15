from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from users.models import User
from django.contrib.auth.hashers import make_password
from users.forms import UserRegistrationForm, UserUpdateForm
from products.forms import ProductCreateForm, ProductUpdateForm, CategoryCreateForm, CategoryUpdateForm
from products.models import Product, ProductCategory
from crud.mixins import ListViewMixin, CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'admin_panel.html')


class UserListView(ListViewMixin):
    model = User
    paginate_by = 5
    template_name = 'ListView/users_list.html'
    context_object_name = 'users'


class ProductListView(ListViewMixin):
    paginate_by = 5
    model = Product
    template_name = 'ListView/product_list.html'
    context_object_name = 'products'


class CategoryListView(ListViewMixin):
    paginate_by = 3
    model = ProductCategory
    template_name = 'ListView/category_list.html'
    context_object_name = 'categorys'


class UserCreate(CreateObjectMixin):
    model = User
    form_class = UserRegistrationForm
    template_name = 'CreateView/user_add.html'
    success_url = reverse_lazy('crud:user_list')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password1'])
        form.instance.is_superuser = form.cleaned_data['is_superuser']
        form.instance.is_staff = form.cleaned_data['is_staff']
        response = super().form_valid(form)
        return response


class UserUpdate(UpdateObjectMixin):
    model = User
    form_class = UserUpdateForm
    template_name = 'UpdateView/user_update.html'
    success_url = reverse_lazy('crud:user_list')


class UserDelete(DeleteObjectMixin):
    model = User
    success_url = reverse_lazy('crud:user_list')


class ProductCreate(CreateObjectMixin):
    model = Product
    form_class = ProductCreateForm
    template_name = 'CreateView/product_add.html'
    success_url = reverse_lazy('crud:product_list')


class ProductUpdate(UpdateObjectMixin):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'UpdateView/product_update.html'
    success_url = reverse_lazy('crud:product_list')


class ProductDelete(DeleteObjectMixin):
    model = Product
    success_url = reverse_lazy('crud:product_list')


class CategoryCreate(CreateObjectMixin):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'CreateView/category_add.html'
    success_url = reverse_lazy('crud:category_list')


class CategoryUpdate(UpdateObjectMixin):
    model = ProductCategory
    form_class = CategoryUpdateForm
    template_name = 'UpdateView/category_update.html'
    success_url = reverse_lazy('crud:category_list')


class CategoryDelete(DeleteObjectMixin):
    model = ProductCategory
    success_url = reverse_lazy('crud:category_list')
