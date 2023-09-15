from django.shortcuts import render
from django.http import HttpResponse
from  .models import Item
from math import ceil

def index(request):
    allProds = []
    catprods = Item.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Item.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'index.html', params)

def about(request):
    return render(request, "about.html")

def contact(request):
    return HttpResponse("We are at about")

def tracker(request):
    return HttpResponse("We are at about")

def product(request):
    return HttpResponse("We are at about")

def checkout(request):
    return HttpResponse("We are at about")

def search(request):
    return HttpResponse("We are at about")
