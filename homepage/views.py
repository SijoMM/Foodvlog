from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:

        prodt=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except:
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':prodt,'ct':cat,'pg':pro})
def prod_details(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prod})

def search(request):
    prod=None
    querry=None
    if 'q' in request.GET:
        querry=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=querry)|Q(desc__contains=querry))
    return render(request,'search.html',{'qr':querry,'pr':prod})