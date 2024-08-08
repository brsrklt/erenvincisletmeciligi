from django.shortcuts import render
from blog.models import Blog, Category, Makinelerimiz, Hakkimizda, İletisim

# Create your views here.

def index(request):
    blogs = Blog.objects.filter(is_active=True).order_by("-id")
    categories = Category.objects.all()
    
    
    context = {
        "blogs": blogs,
        "categories" : categories
    }
    return render(request, "blog/index.html", context)


def makineler(request):    
    context = {
        "makineler": Makinelerimiz.objects.all(),
    }
    return render(request, "blog/makineler.html", context)


def hakkimizda(request):
    context = {
        "hakkimizdas": Hakkimizda.objects.order_by("-id"),
    }
    return render(request, "blog/hakkimizda.html", context)



def iletisim(request):
    context = {
        "iletisims": İletisim.objects.order_by("-id"),
    }
    return render(request, "blog/iletisim.html", context)



def blog_details(request, slug):    
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog":blog
    }

    return render(request, "blog/blog-detail.html", context)


def blogs_by_category(request,slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories" :Category.objects.all(),
        "selected_category" : slug
    }
    return render(request, "blog/index.html", context)