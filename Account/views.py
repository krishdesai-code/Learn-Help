from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password

def registerPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        hased_pass = make_password(password)

        User.objects.create(
            name=name,
            email=email,
            password=hased_pass,
        )
        return redirect("loginPage")
    return render(request,"account/register.html")

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get("email") 
        password = request.POST.get("password")

        hased_pass = make_password(password)
        user = User.objects.get(email=email,password=hased_pass)
        
        if(user):
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            request.session['name'] = user.name
            return redirect("home")
        else :
            return render(request,"account/login.html",{'error' : 'Invalid email or password'})

    return render(request,"account/login.html")

def homePage(request):
    return render(request,"account/home.html")

def logoutPage(request):
    request.session.flush()
    return redirect("/")