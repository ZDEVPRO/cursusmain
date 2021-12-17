from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

#from home.models import FAQ
from django.utils.crypto import get_random_string

from home.models import FAQ, Setting
from order.models import Order, OrderProduct
from product.models import Category, Comment
from user.models import UserProfile
from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm



@login_required(login_url='/login')
def index(request):
   # return HttpResponse("User app")
     category = Category.objects.all()
     current_user = request.user



     profile = UserProfile.objects.get(user_id=current_user.id)
     context = {'category': category,
                #'order_product': order_product,
                'profile': profile,}
     return render(request, 'userprofile.html', context)



def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error! User name or Password is incorrect")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    setting = Setting.objects.all()
    context = {'category': category,
               'setting': setting}
    return render(request, 'login.html', context)


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            #Create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')

            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.all()
    context = {'category': category,
               'form': form,
               'setting': setting
               }
    return render(request, 'signup_form.html', context)


@login_required(login_url='/login')
def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login') #check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        setting = Setting.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
             'category': category,
             'user_form': user_form,
             'profile_form': profile_form,
             'setting': setting
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was succesfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below. <br>' + str(form.errors))
            return HttpResponseRedirect('user/password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form, 'category': category,
                                                      'setting':setting})



@login_required(login_url='/login')
def user_orders_product(request):
    category = Category.objects.all()
    setting = Setting.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    context = { 'category': category,
                'order_product': order_product,
                'setting' : setting,

    }
    return render(request, 'user_order_product.html', context)


@login_required(login_url='/login')
def user_order_product_detail(request,id, oid):
    category = Category.objects.all()
    setting = Setting.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitem = OrderProduct.objects.filter(id=id,user_id=current_user.id)
    context = { 'category': category,
                'order': order,
                'orderitem': orderitem,
                'setting' : setting,
    }
    return render(request, 'user_order_product_detail.html', context)

@login_required(login_url='/login')
def user_comments(request):
    category = Category.objects.all()
    setting = Setting.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comments': comments,
               'setting': setting,
               }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, "Comment has been deleted!")
    return HttpResponseRedirect("/user/comments")


def faq(request):
    category = Category.objects.all()
    setting = Setting.objects.all()
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    context = {'category': category,
                'faq': faq,
                'setting': setting
                }
    return render(request, 'faq.html', context)