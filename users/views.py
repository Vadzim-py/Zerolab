from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, UserSetPassForm
from products.models import UserBookmarks
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have been successfully log in')
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
               'form': form,
               'bookmarks': UserBookmarks.objects.all()
               }
    return render(request, 'users/profile.html', context)


@login_required
def setpass(request):
    if request.method == "POST":
        form = UserSetPassForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserSetPassForm(user=request.user)
    context = {'form': form}
    return render(request, 'users/setpass.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
