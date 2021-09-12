from django.shortcuts import redirect, render,HttpResponse
from groo.models import NewUser
# Create your views here.
def index(request):
    return render(request,'Login.html')

def signup(request):
    return render(request,'signup.html')

def formsignup(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=NewUser(username=name,email=email,password=password)
        user.save()
    
    return redirect('index')