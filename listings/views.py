from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

from listings.choices import bedroom_choices,price_choices,state_choices

# Create your views here.
def index(request): #for all views, render html request
    # import all listings from db in reverse(- for reverse) order of date, to show only those listings where is_published is true, use filter
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    
    # set how many listings to show per page
    paginator = Paginator(listings,6) 
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)



def listing(request, listing_id): #for all views, render html request
    # pk represents primary key
    # 404 will show Page Not Found page
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing': listing,
        'photos': [listing.photo_1,listing.photo_2,listing.photo_3,listing.photo_4,listing.photo_5,listing.photo_6]
    }
    return render(request, 'listings/listing.html', context)



def search(request): #for all views, render html request
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET: # if keywords in form is not null
        keywords = request.GET['keywords'] # get the text in keyword textfield, looking at form fields name, like 'keywords'
        if keywords: # if keywords in form is not null
            queryset_list = queryset_list.filter(description__icontains=keywords) # if description contains same words in keywords

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state != "State (Any)": # if State (All) is selected, it will show all listings
                queryset_list = queryset_list.filter(state__iexact=state)

    
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms  != "Bedrooms (Any)":
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price  != "Max Price (Any)":
            queryset_list = queryset_list.filter(price__lte=price)

    # set how many listings to show per page
    paginator = Paginator(queryset_list,6) 
    page = request.GET.get('page')
    paged_queryset_list = paginator.get_page(page)

    context = {
        'listings': paged_queryset_list,
       'state_choices': state_choices,
       'bedroom_choices': bedroom_choices,
       'price_choices': price_choices,
       'values': request.GET # to keep search data in textfield/box
    }
    return render(request, 'listings/search.html',context)
