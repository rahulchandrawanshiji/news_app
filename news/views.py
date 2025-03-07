# from googletrans.models import Translated
from .models.photo import Photo
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.customer import Customer
# from django.contrib.auth import authenticate,login,logout
from .models.aduestiment import Aduestiment
from .models.new import News
from .models.new import sendEmail,SendEmail
from .models.video import Item
# Create your views here.
import requests
import json

def index(request):
    # if request.method =='GET':

            ad=Aduestiment.objects.all()
            n=News.objects.all()
            se=request.session.get('customer')
            # a=request.COOKIES('cid')
            # print(se)
            URL ='http://newsapi.org/v2/top-headlines?country=in&apiKey=44ddea6e1a5444518ea8d5b9b065ed4e'
            r =requests.get(url= URL)

            data = json.loads(r.content)
    
            parm={}
            parm['data']=data
          
            # print(translater.detect(data))
            # print("Translated From Hindi :",translater.translate(data))
            parm['ad']=ad  
            parm['n']=n
            parm['se']=se
            # print(parm)
            return render(request,'index.html',parm)
    # else:
       
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        value ={
            'name':name,
             'phone':phone,
             'email':email
        }
        customers=Customer(name=name,phone=phone,email=email,password=password)
        error_massage =validateCustomer(customers)
        if not error_massage:
            customers.save()
            print(name,phone,email,password)
            return redirect('homepage')
        else:
            data = {
                'error':error_massage,
                'values':value
                }
            return render(request , 'signup.html',data)

def validateCustomer(customers):
    #   customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password);
        error_massage=None;
        if(not customers.name):
            error_massage='First Name Required  !!!'
        elif len(customers.name) < 4: 
            error_massage='First Name must be and also changes to words  to thee same subject  4 char long'
        # elif not customers.last_name:
        #     error_massage='Last Name Required  !!!'
        # elif len(customers.last_name) < 4:
        #     error_massage='Last Name must be 4 char long'
        elif not customers.phone:
            error_massage='Phone Number Required  !!!'
        elif len(customers.phone) < 10:
            error_massage='Phone Number must be 10'
        elif len(customers.email) <5 :
            error_massage='Email  Required  !!!'
        elif not customers. password:
            error_massage='Password must be Requied !!!'
        
        elif len(customers.password) <5:
            error_massage='Password  must be 6 char long'
        
        elif customers.isExists():
            error_massage='Email Address Alredy registered...'  
        return error_massage  
    


def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer =Customer.get_customer_by_email(email)
        error_message = None
        if customer:
           pas =Customer.get_customer_by_password(password)
           print(pas)
           if pas:
            #    response.set_cookie('cid','customer')
               v=request.session['customer']=email
               print(v)
               content="You are successful login in Aazadmedia News"
            #    SendEmail(email,content)
               return redirect('homepage')
           else:
                error_message='Email or Password invalid !!!'

        else:
            error_message='Email or Password invalid !!!'
        return render(request,'login.html',{'error' : error_message})

def about(request): 
    return render(request,'about.html')
def contact(request):
    if request.method =='GET':
        return render(request,'contact.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('massge')
        print(name,email,content)
        sendEmail(email,content)
        return redirect('homepage')
def search(request):
    query = request.GET.get('query')

    all=News.objects.filter(title=query)
    print(all)
    parem={'all':all}
    return render(request,'search.html',parem)
def photo(request):
    if request.session.has_key('customer'):
        URL ='http://newsapi.org/v2/top-headlines?country=in&apiKey=44ddea6e1a5444518ea8d5b9b065ed4e'
        r =requests.get(url= URL)

        data = json.loads(r.content)
    
        # photos=Photo.objects.all()
        parm={}
        parm['data']=data

        return render(request,'photo.html',parm)
    else:
        return render(request,'login.html')


def vedio(request):
    if request.session.has_key('customer'):

        obj=Item.objects.all()
        return render(request , 'video.html',{'obj':obj})
    else:
        return render(request,'login.html')


def state(request):
    states=request.GET.get('N')
    print(states)
    # n=News.objects.filter(category=states)
    URL ='http://newsapi.org/v2/top-headlines?country=in&apiKey=44ddea6e1a5444518ea8d5b9b065ed4e'
    r =requests.get(url= URL)
    data = json.loads(r.content)
    # n=(data['articles']['source.name']==states)
    parm={}
    parm['data']=data
    for i in data['articles']:
        # parm['v']=i


        if(i==states):
            print(i)

    parm['states']=states

    return render(request,'list.html',parm)

# def Australia(request):
#     if request.session.has_key('customer'):
    
#         URL ='http://newsapi.org/v2/top-headlines?country=au&apiKey=44ddea6e1a5444518ea8d5b9b065ed4e'
#         r =requests.get(url= URL)
#         data = json.loads(r.content)
#         parm={}
#         parm['data']=data
#         return render(request,'list.html',parm)  
#     else:
#         return render(request,'login.html')
     

def logout(request):
    request.session.clear()
    return redirect('homepage')
def country(request):
    if request.session.has_key('customer'):
    
        URL ='http://newsapi.org/v2/top-headlines?country=in&apiKey=44ddea6e1a5444518ea8d5b9b065ed4e'
        r =requests.get(url= URL)
        data = json.loads(r.content)
        parm={}
        parm['data']=data
        return render(request,'list.html',parm)
    else:
        return render(request,'login.html')
