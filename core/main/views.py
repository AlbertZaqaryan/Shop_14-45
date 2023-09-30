from django.shortcuts import render
from .models import HomeLogo, HomeCarusel, Category, SubCategory,  Product

def all_for_site():
    one_logo = HomeLogo.objects.all().first()
    return one_logo


def index(request):
    active_carusel = HomeCarusel.objects.all().first()
    carusel_list = HomeCarusel.objects.all()[1:]
    category_list = Category.objects.filter()
    product_list = Product.objects.all()
    sub_category = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'one_logo':all_for_site(),
        'action':'index',
        'active_carusel':active_carusel,
        'carusel_list':carusel_list,
        'category_list':category_list,
        'product_list':product_list,
        'sub_category':sub_category


    })


def index_filter(request, id):
    active_carusel = HomeCarusel.objects.all().first()
    carusel_list = HomeCarusel.objects.all()[1:]
    category_list = Category.objects.filter()
    product_list = SubCategory.objects.filter(pk=id)
    sub_category = SubCategory.objects.all()
    return render(request, 'main/index_filter.html', context={
        'one_logo':all_for_site(),
        'action':'index',
        'active_carusel':active_carusel,
        'carusel_list':carusel_list,
        'category_list':category_list,
        'product_list':product_list,
        'sub_category':sub_category

    })

def blog_single(request):
    return render(request, 'main/blog-single.html', context={
        'one_logo':all_for_site(),
        'action':'blog_single'

    })

def blog(request):
    return render(request, 'main/blog.html', context={
        'one_logo':all_for_site(),
        'action':'blog'

    })

def cart(request):
    return render(request, 'main/cart.html', context={
        'one_logo':all_for_site(),
        'action':'cart'

    })

def checkout(request):
    return render(request, 'main/checkout.html', context={
        'one_logo':all_for_site(),
        'action':'checkout'

    })

def contact_us(request):
    return render(request, 'main/contact-us.html', context={
        'one_logo':all_for_site(),
        'action':'contact_us'

    })

def login(request):
    return render(request, 'main/login.html', context={
        'one_logo':all_for_site(),
        'action':'login'

    })

def product_details(request):
    return render(request, 'main/product-details.html', context={
        'one_logo':all_for_site(),
        'action':'product_details'

    })

def shop(request):
    return render(request, 'main/shop.html', context={
        'one_logo':all_for_site(),
        'action':'shop'

    })

def error(request):
    return render(request, 'main/404.html', context={
        'one_logo':all_for_site(),
        'action':'error'

    })

