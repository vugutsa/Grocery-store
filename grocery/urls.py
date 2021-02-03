# # from django.conf.urls import url
# from django.urls import path,include
# from . import views
# from django.contrib.auth.views import LoginView, LogoutView 
# from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns=[
#     # url('^$',views.welcome,name = 'welcome'),
#     path('', views.index,name='index'),
#     path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_grocery,name = 'pastGrocery'),
#     path('products/<slug>',views.ProductDetails,name='products'),
#     path('add-to-cart/<slug>',views.add_to_cart,name='add-to-cart'),
#     path('search/', views.search_results, name='search_results'),
#     path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
#     path('accounts/register/', views.registration, name='register'),
#     path('about/', views.about, name='about'),
#     path('checkout/', views.checkout, name='checkout')
# ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)