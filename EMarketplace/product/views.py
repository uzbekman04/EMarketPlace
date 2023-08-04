from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from cart.forms import CartAddProductForm

# Create your views here.
class HomePage(generic.ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'

class DetailsPage(generic.DetailView):
    model = Product
    template_name = 'product/about.html'
    context_object_name = 'product'

def CategoryPage(request,category_slug):
    categories = Category.objects.all
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request,'product/category.html',{
        'category':category,
        'categories':categories,
        'products':products
    })




def homeview(request):
    products = Product.objects.all()
    categories =Category.objects.all()
    context ={
        'products' : products,
    'categories' : categories
    }
    return render(request,template_name='product/home.html',context=context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/about.html', {'product': product, 'cart_product_form': cart_product_form})




