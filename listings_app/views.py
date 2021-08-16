from django.shortcuts import render

# Create your views here.

def index_view(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'listing_app/listings.html', contex)

def listing_view(request, listing_id):

    contex = {
        'key': 'value',
    }
    return render(request, 'listing_app/listing.html', contex)

def search_view(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'listing_app/search.html', contex)
