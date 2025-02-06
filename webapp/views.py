from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth #logging out
from django.contrib.auth import authenticate #authenticate users
# from django.http import HttpResponse
# Create your views here.

# Homepage
def home(request):
    # return HttpResponse('HelloWorld!')
    return render(request,'webapp/index.html') 

# Register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form':form}
    
    return render(request,'webapp/register.html',context=context)

#log in
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)
        
        if user is not None:
            auth.login(request,user)

            #return redirect('')
    
    context = {'form':form}
    return render (request, 'webapp/my-login.html',context=context)

# logout
def user_logout(request):
    auth.logout(request)
    return redirect('my-login')
