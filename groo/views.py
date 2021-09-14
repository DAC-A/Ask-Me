from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return HttpResponse("Home Page abhi tk nhi bna h...")

def signup(request):
    return render(request,'index.html')

def formsignup(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
    
    return redirect('index')

def login(request):
    return render(request,'index.html')

def formlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse('Hello')
        else:
            return HttpResponse('Aap kaun')

    
    return HttpResponse('Kuch to gadbad h daya')
