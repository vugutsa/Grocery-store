from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import *
import json
from django.http import JsonResponse
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    date = dt.date.today()
    day = convert_dates(date)
    products = Product.objects.all()
    context = {'products':products}
    
    return render(request, 'all-grocery/index.html',{"date": date, 'products':products})


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data[items]

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'all-grocery/cart.html', {'product':product})


def about(request):
    return render(request,'all-grocery/about.html')
def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_grocery(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-grocery/past-news.html', {"date": date})
def checkout(request):
    return render(request, 'all-grocery/checkout.html')
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)
def search_results(request):
    
    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        searched_products = Product.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-grocery/search.html',{"message":message,"products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-grocery/search.html',{"message":message})
    
def get_product(request, id):
    product = Product.objects.get(pk=id)

    return render(request, 'product.html', {'product':product})


    
def ProductDetails(request):
    context = {}
    return render('product.html')

def updateProduct(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderProduct, created = orderProduct.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderProduct.quantity = (orderProduct.quantity + 1)
    elif action == 'remove':
        orderProduct.quantity = (orderProduct.quantity - 1)
    orderProduct.save()
    if orderProduct.quantity <= 0:
        orderProduct.delete()
    return JsonResponse('product was added', safe=False)  