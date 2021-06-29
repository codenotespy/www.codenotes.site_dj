from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from blogapp.models import Profile

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash





def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
#            form.save()
#            return redirect('/')
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('/')
#            return redirect(reverse('home'))
        else:
            messages.error(request, 'I think something is wrong')
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {'form':form})


def afterlogin(request):
    messages.info(request, "You are now logged in.")
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('/')


def afterlogout(request):
    messages.info(request, "You are now logged out.")
    return redirect('/')
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been updated.')
            return redirect('profile_update')
    else:
        form = ProfileUpdateForm(instance=request.user)
        
    return render(request, "accounts/profile.html", {'form':form, 'profile':profile})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.info(request, 'Your password has been updated successfully!')
#            messages.success(request, 'Your password has been updated successfully!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })



#def change_username(request):
#    if request.method == 'POST':
#       form = PasswordChangeForm(request.user, request.POST)
#        if form.is_valid():
#            if User.objects.filter(username=newusername).exists():
#                raise forms.ValidationError(u'Username "%s" is not available.' % newusername)
#
#            user = User.objects.get(username = username)
#            user.username = newusername
#            user.save()
#            update_session_auth_hash(request, user)  # Important!
#            messages.success(request, 'Your username was successfully updated!')
#            return redirect('change_username')
#    else:
#        form = PasswordChangeForm(request.user)
            
            
            
            