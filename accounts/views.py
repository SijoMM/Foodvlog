from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    return render(request,'login.html')
def reg(request):
    if request.method=='POST':
        username=request.POST['usernamename']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        phoneno = request.POST['phone']
        email = request.POST['email']
        pass1= request.POST['pass']
        pass2 = request.POST['pass2']
        user=User.objects.create_user(username=username,first_name=firstname,password=pass1,email=email,last_name=lastname,phone_no=phone,gender=gender)
    return render(request,'registration.html')