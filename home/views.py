import json

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
# Create your views here.

from home.models import Setting, ContactForm, ContactMessage
from home.forms import SearchForm
from product.models import Category, Product, Images, Comment
from user.models import UserProfile


def index(request):
    return render(request, 'index/base.html')


def category_product(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.all()
    product_slider = Product.objects.all().order_by('?')[:3]
    product_picked = Product.objects.all().order_by('id')[:3]
    product_latest = Product.objects.all().order_by('-id')[:3]
    catdata = Category.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 9)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'catdata': catdata,
        'products': products,
        'setting': setting,
        'product_latest': product_latest,
        'product_picked': product_picked,
        'product_slider': product_slider,
    }
    return render(request, 'category_detail/base.html', context)


########################################################################################################################
########################################################################################################################


########################################################################################################################
########################################################################################################################
def product_detail(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.all()
    product_picked = Product.objects.all().order_by('?')[:8]
    product_latest = Product.objects.all().order_by('-id')[:8]
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    user = UserProfile.objects.all()
    context = {
        'category': category,
        'product': product,
        'images': images,
        'comments': comments,
        'setting': setting,
        'product_latest': product_latest,
        'product_picked': product_picked,
        'user': user
    }
    return render(request, 'course_detail/base.html', context)


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            setting = Setting.objects.all()
            context = {
                'products': products,
                'query': query,
                'category': category,
                'setting': setting,
            }
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for rs in products:
            products_json = {}
            products_json = rs.title
            results.append(products_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def explore(request):
    return render(request, 'explore/base.html')


def saved_courses(request):
    return render(request, 'saved_courses/base.html')
