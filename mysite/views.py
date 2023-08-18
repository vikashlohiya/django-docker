
from django.shortcuts import render



def home_page(request):
    return render(request, 'home.html')
def about_us(request):   
    return render(request, 'about.html',{'name':'vikash','clist':12})

def contact(request):   
    return render(request, 'contact.html')

def product(request):   
    return render(request, 'product.html')

