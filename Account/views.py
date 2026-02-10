from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


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
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                request.session['name'] = user.name
                return redirect("home")
            else:
                return render(request, "account/login.html", {
                    'error': 'Invalid email or password'
                })
        except User.DoesNotExist:
            return render(request, "account/login.html", {
                'error': 'Invalid email or password'
            })
    return render(request, "account/login.html")

def homePage(request):
    if not request.session.get('user_id'):
        return redirect("loginPage")
    return render(request,"account/home.html")

def logoutPage(request):
    request.session.flush()
    return redirect("/")