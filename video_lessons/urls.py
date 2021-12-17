from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views
from order import views as OrderViews
from user import views as UserViews
from home.views import *

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # path('about/', views.aboutus, name='aboutus'),
    # path('contact/', views.contactus, name='contactus'),
    # path('contact/',views.contactnote, name='contactnote'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('explore/', views.explore, name='explore'),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('login/', UserViews.login_form, name='login_form'),
    path('logout/', UserViews.logout_func, name='logout_func'),
    path('signup/', UserViews.signup_form, name='signup_form'),
    path('faq/', UserViews.faq, name='faq'),

    path('cart/', OrderViews.shopcart, name='shopcart'),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_product, name='category_product'),
    path('course-detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('saved-courses/', views.saved_courses, name='saved_courses'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
