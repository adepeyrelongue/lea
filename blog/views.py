from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, "home.htm",{'post_list' : post_list})