from django.shortcuts import render,get_object_or_404
from garments.models import Formalshirt,Casualshirt,Tshirt,IndianWear,WesternWear,FootWear,BoysClothing,GirlsClothing,Brand
from django.db.models import Q
from django.contrib import messages
from garments.form import ContactForm
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        name=request.POST.get('contact_name')
        email=request.POST.get('contact_email')
        content=request.POST.get('content')
        subject='Hello I am from MyGarmentShop'
        from_email=settings.EMAIL_HOST_USER
        user_email=email
        to_list=[user_email,from_email]
        send_mail(subject,content,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')

    
    return render(request,'contactus.html',{'form':form})
    
    
def thankyou(request):
    return render(request,'thankyou.html')

def formalshirt(request):
    lst=Formalshirt.objects.all()
    return render(request,'formalshirt.html',{'lst':lst})

def casualshirt(request):
    lst1=Casualshirt.objects.all()
    return render(request,'casualshirt.html',{'lst1':lst1})

def tshirt(request):
    lst2=Tshirt.objects.all()
    return render(request,'tshirt.html',{'lst2':lst2})

def indianwear(request):
    lst3=IndianWear.objects.all()
    return render(request,'indianwear.html',{'lst3':lst3})

def westernwear(request):
    lst4=WesternWear.objects.all()
    return render(request,'westernwear.html',{'lst4':lst4})

def footwear(request):
    lst5=FootWear.objects.all()
    return render(request,'footwear.html',{'lst5':lst5})

def boysclothing(request):
    lst6=BoysClothing.objects.all()
    return render(request,'boysclothing.html',{'lst6':lst6})

def girlsclothing(request):
    lst7=GirlsClothing.objects.all()
    return render(request,'girlsclothing.html',{'lst7':lst7})

def brand(request):
    lst8=Brand.objects.all()
    return render(request,'brand.html',{'lst8':lst8})

def search_list(request):
    q=request.GET.get('query')
    if q:
        match1=Formalshirt.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))

    if match1:
        return render(request,'search_list.html',{'match1':match1})
    else:
        messages.error(request,'no result found')
        return render(request,'search_list1.html')
    return render(request,'search_list.html')

lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(Formalshirt,id=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_item':len(lst),'tot_price':sum(price)})








    
    
