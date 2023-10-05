from django.shortcuts import render, redirect
from .models import (HomeLogo, HomeCarusel, 
                    Category, SubCategory,  Product,
                    Filter, Filter_product, Card, Contact)
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def all_for_site():
    one_logo = HomeLogo.objects.all().first()
    return one_logo


def index(request):
    active_carusel = HomeCarusel.objects.all().first()
    carusel_list = HomeCarusel.objects.all()[1:]
    category_list = Category.objects.filter()
    product_list = Product.objects.all()
    sub_category = SubCategory.objects.all()
    filter_list = Filter.objects.all()
    filter_products = Filter.objects.filter()
    return render(request, 'main/index.html', context={
        'one_logo':all_for_site(),
        'action':'index',
        'active_carusel':active_carusel,
        'carusel_list':carusel_list,
        'category_list':category_list,
        'product_list':product_list,
        'sub_category':sub_category,
        'filter_list':filter_list,
        'filter_products':filter_products


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
    card_list = Card.objects.all()
    return render(request, 'main/cart.html', context={
        'one_logo':all_for_site(),
        'action':'cart',
        'card_list':card_list

    })

def add_to_cart(request):
    if request.method == "POST":
        item = request.POST.get('item')
        one_prod = Product.objects.get(id=item)
        Card.objects.create(prod=one_prod)
        return redirect('index')


def delete_to_cart(request):
    if request.method == "POST":
        item = request.POST.get('item')
        Card.objects.filter(id=item).delete()
        return redirect('cart')

def checkout(request):
    return render(request, 'main/checkout.html', context={
        'one_logo':all_for_site(),
        'action':'checkout'

    })

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('index')
    return render(request, 'main/contact-us.html', context={
        'one_logo':all_for_site(),
        'action':'contact_us'

    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

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

