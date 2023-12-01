from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import *


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/home/')


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        login(request, user)
        return redirect("/")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
