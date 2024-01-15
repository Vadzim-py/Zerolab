from django import forms
from products.models import Product, ProductCategory


class ReviewForm(forms.Form):
    item_review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-1', 'placeholder': 'What do you think about this product?'}))


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter product name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter product description'}))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)
    url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter a link to your product'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control py-3', 'placeholder': 'Select a category'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'url', 'category')


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'}))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)
    url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control py-3'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'url', 'category')


class CategoryCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter category name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter category description'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class CategoryUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
