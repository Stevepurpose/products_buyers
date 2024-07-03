from django.urls import path
from . import views
 

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/buyers/', views.buyers, name='buyers'),
    path('products/orders', views.joins, name='orders'),
    path('products/prodetails/<int:productID>', views.proDetails, name='proDetails'),
    path('products/buyers/buyerdetails/<int:id>', views.buyerDetails, name='buyerDetails'),
    path('', views.main, name='main'),

]