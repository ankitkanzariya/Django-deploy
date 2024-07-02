from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.login,name='login'),
   path('blog_list/',views.blog_list,name='blog_list'),
   path('product/',views.product,name='product'),
   path('testimonial/',views.testimonial,name='testimonial'),
   path('logout/',views.logout,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('change-password/',views.change_password,name='change-password'),
   path('forgot-password/',views.forgot_password,name='forgot-password'),
   path('verify-otp/',views.verify_otp,name='verify-otp'),
   path('update-password/',views.update_password,name='update-password'),
   path('add-product/',views.add_product,name='add-product'),
   path('view-product/',views.view_product,name='view-product'),
   path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
   path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),
   path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'),
   path('product-details/<int:pk>/',views.product_details,name='product-details'),
   path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
   path('wishlist/', views.wishlist, name='wishlist'),
   
   path('remove-from-wishlist/<int:pk>',views.remove_from_wishlist,name='remove-from-wishlist'),
   path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'), 
   path('cart/',views.cart,name='cart'), 
   path('remove-from-cart/<int:pk>',views.remove_from_cart,name='remove-from-cart'), 
   path('change-qty/<int:pk>',views.change_qty,name='change-qty'), 
   path('create-checkout-session/', views.create_checkout_session, name='payment'),
   path('success.html/', views.success,name='success'),
   path('cancel.html/', views.cancel,name='cancel'),
   path('myorder/',views.myorder,name='myorder'),
   path('ajax/validate_email',views.validate_signup,name='validate_email'),
   path('seller-myorder/',views.seller_myorder,name='seller-myorder'),




]
