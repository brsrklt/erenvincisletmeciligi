
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("makineler/", views.makineler, name="makineler"),
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("iletisim/", views.iletisim, name="iletisim"),

    path("category/<slug:slug>",views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]

