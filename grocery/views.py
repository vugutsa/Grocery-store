from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Product,OrderProduct,Order
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    date = dt.date.today()
    day = convert_dates(date)
    products = Product.objects.all()
    print(products)
    context = {'products':products}
    
    return render(request, 'all-grocery/index.html',{"date": date, 'products':products})


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
def ProductDetails(request):
    context = {}
    return render('product.html')
def add_to_cart(request,slug):
    product = get_object_or_404(Product, slugs=slug)
    order_product = OrderProduct.objects.create(product=product)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            
    else:
        order = Order.objects.create(user=request.user)
        order.product.add(order_product)
        return redirect("grocery:products",kwargs={'slug': slug})
        
     