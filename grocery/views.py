from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')
def index(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Grocery bought on {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return render(request, 'all-grocery/index.html', {"date": date,})
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

def search_results(request):
    
    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        searched_products = Product.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-grocery/search.html',{"message":message,"products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-grocery/search.html',{"message":message})
    
def store(request):
    context 