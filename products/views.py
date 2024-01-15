from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from products.models import ProductCategory, Product, UserBookmarks, Rate
from products.forms import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def products(request, category_id=None):
    articles = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': ProductCategory.objects.all(),
        'products': page_obj,
        'page_obj': page_obj,
        }
    return render(request, 'products/products.html', context)


@login_required
def product_review(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            star_rating = request.POST.get('rating')
            item_review = form.cleaned_data['item_review']
            item_reviews = Rate(
                user=request.user, product=product,
                rating=star_rating, overview=item_review
            )
            item_reviews.save()
            messages.success(request, 'Thanks for your review!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ReviewForm()
    rating_details = Rate.objects.filter(product=product)
    context = {'reviews': rating_details,
               'form': form
               }
    return render(request, 'review_page.html', context)


@login_required
def bookmark_add(request, product_id):
    product = Product.objects.get(id=product_id)
    bookmark = UserBookmarks.objects.filter(user=request.user, product=product)
    if not bookmark.exists():
        UserBookmarks.objects.create(user=request.user, product=product)
    else:
        basket = bookmark.first()
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def bookmark_delete(request, bookmark_id):
    basket = UserBookmarks.objects.get(id=bookmark_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
