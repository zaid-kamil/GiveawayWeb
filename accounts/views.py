from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from products.models import Giveaway, GiveawayEntry, Product
from .forms import UserLoginForm, UserRegistration


# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "login.html", {"forms": form})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/login/')
def show_dash(request):
    entries = GiveawayEntry.objects.filter(user=request.user.id)
    giveaways = Giveaway.objects.all()
    products = Product.objects.all()
    context = {
        'entries': entries,
        'giveaways': giveaways,
        'products': products
    }
    return render(request, 'profile_dashboard.html', context)
