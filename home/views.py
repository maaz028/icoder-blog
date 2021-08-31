from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import contact
from blogapp.models import post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def about_us(request):
    return render(request, 'home/about.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')        
        if name!='' and email != '' and phone !='':
            contact_data = contact(name = name, email= email, phone = phone, query_txt = text)
            contact_data.save()
            messages.success(request, 'Contact details updated.')        
        else:
            messages.error(request, 'Provide complete details.')
    return render(request, 'home/contact.html')

def handle_signup(request):
    if request.method == 'POST':
        print('signup')
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']      
        users = User.objects.all()        
        for user in users:  
            if str(user) == username:  
                messages.error(request,'Username already taken')
                return redirect('/')
            
        user = User.objects.create_user(username,email,pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        
        messages.success(request,'Your ICoder account has created successfully !')   
        return redirect('/')
    
def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:  
            messages.error(request,'Login does not exits')
            return redirect('/')
        
        login(request,user)
        messages.success(request,'You are Successfully logged in')
        return redirect('/',{'user':user})
        # return render(request,'home/home.html',{'user':user})
            
def handle_logout(request):
    logout(request)
    messages.error(request,'You have logged out')
    return redirect('/')