from django.shortcuts import render
from .models import Post, Product, FirstPage
# Create your views here.
def home(request):
    product_list = Product.objects.all()
    first_page = FirstPage.objects.all()[0]
    return render(request, "home.html", {'product_list' : product_list, 'first_page' : first_page})

def post_list(request):
    post_list = Post.objects.all()
    product_list = Product.objects.all()
    return render(request, "post_list.html",{'post_list' : post_list,'product_list' : product_list})

def post_detail(request,slug):
    post_detail = Post.objects.get(slug=slug)
    product_list = Product.objects.all()
    return render(request, "post_detail.html",{'post_detail' : post_detail,'product_list' : product_list})