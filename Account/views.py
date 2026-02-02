from django.shortcuts import render

def registerPage(request):
    return render(request,"account/register.html")

def loginPage(request):
    return render(request,"account/login.html")
