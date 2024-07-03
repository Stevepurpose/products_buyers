from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader
from .models import Product, Buyer

# Create your views here.
def products(request):
    template=loader.get_template('transactions.html')
    products = Product.objects.all().values()
    context={
           'products':products
    }

    return HttpResponse(template.render(context, request))


def buyers(request):
    template=loader.get_template('buyers.html')
    buyers = Buyer.objects.all().values()
    context={
           'buyers':buyers
    }

    return HttpResponse(template.render(context, request))


def joins(request):
    template = loader.get_template('orders.html')
    orders = Buyer.objects.select_related('productID').all()
    context={
           'orders':orders
    }
    return HttpResponse(template.render(context, request))

def proDetails(request, productID):
    myProduct = Product.objects.get(productID=productID)
    template = loader.get_template('prodetails.html')
    context={
        'myProduct':myProduct
    }
    return HttpResponse(template.render(context, request))


def buyerDetails(request, id):
    myBuyer = Buyer.objects.get(id=id)
    template = loader.get_template('buyerdetails.html')
    context={
        'myBuyer':myBuyer
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

