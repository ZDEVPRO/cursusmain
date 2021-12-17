from home.models import Logo
from django.shortcuts import render

from home.models import Setting
from product.models import Category, Product, Images, Comment
from user.models import UserProfile


def selected_courses(request):
    category = Category.objects.all()
    scourses_slider = Product.objects.all().order_by('id')
    scourses_latest = Product.objects.all().order_by('-id')[:8]
    scourses_picked = Product.objects.all().order_by('?')[:8]
    page = "home"
    context = {
        'category': category,
        'scourses_slider': scourses_slider,
        'scourses_latest': scourses_latest,
        'scourses_picked': scourses_picked,
        'page': page,

    }
    return context


def logo(request):
    logo_title = Logo.objects.all().order_by('-id')[:1]

    context = {
        'logo_title': logo_title,

    }
    return context
