from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.registerPage,name="registerPage"),
    path("login/",views.loginPage,name="loginPage"),
    path("logout/",views.logoutPage,name="logout"),
    path("home/",views.homePage,name="home")
]
