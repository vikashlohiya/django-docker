from django.shortcuts import render,redirect

# Create your views here.


from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .models import Product

from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('pass')
        
        error=[];
        if name=='':
           error.append('Username can not be blank') 
        if password=='':
           error.append('Pass can not be blank') 
       
        

        if name!='' and password!='' :
           userexist = User.objects.filter(username=name)
           if userexist.exists():
               error.append('Username taken') 
               return render(request, 'product/register.html',{'error':error})  

           user=User.objects.create_user(username=name,password=password)
           user.save()
           return render(request, 'product/login.html',{'success':1 })
        else:
           return render(request, 'product/register.html',{'error':error}) 
    return render(request, 'product/register.html')       
def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('pass')
        
        error=[];
        if name=='':
           error.append('Username can not be blank') 
        if password=='':
           error.append('Pass can not be blank') 
       
        

        user = auth.authenticate(username=name, password=password)
        if user is not None:
             auth.login(request,user)
              
             print("login")
             print(user.is_authenticated )
             return redirect('/product/shop')  # Replace 'home' with your desired URL name after login
        else:
            print("invalid")  
            if len(error)==0:
               error.append('Invalid login credentials')
            return render(request, 'product/login.html', {'error': error})
      
    return render(request, 'product/login.html')  
@login_required   
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        image_file = request.FILES.get('image')
        print("image upload")
        print(image_file)
        #uploaded_image = Product.objects.create(image=image_file)

        # Get the URL of the uploaded image
        #image_url = uploaded_image.image.url
        print(image_file)
        error=[];
        if name=='':
           error.append('Name can not be blank') 
        if desc=='':
           error.append('Desc can not be blank') 
        if price=='':
           error.append('Price can not be blank') 

        if name!='' and desc!='' and price!='' :
           product = Product()
           product.name = name
           product.desc = desc
           product.price=price
           product.image=image_file
           
           product.save()
           
           return render(request, 'product/product.html')
        else:
           return render(request, 'product/product.html', {'error': error})
    else:
        
        return render(request, 'product/product.html')
@login_required
def shop(request):
    all_objects = Product.objects.all()
    search_query = request.GET.get('search_query')
    if search_query:
       query=Q(name__icontains=search_query) | Q(desc__icontains=search_query)    
       all_objects = all_objects.filter(query) 

    paginator = Paginator(all_objects, 3)  # Number of objects per page
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number) 
    print("vikash")
    print(search_query)
   
    if search_query == None:
       search_query=""
    
    return render(request, 'product/shop.html',{"product":page_objects,"search_query": search_query})

def logout(request):
    auth.logout(request)
    return redirect('/about') 