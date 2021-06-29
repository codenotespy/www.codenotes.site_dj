from django.shortcuts import render, redirect
from .forms import RegisterForm, PasswordChangeForm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash





def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
        
    return render(response, "register/register.html", {'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
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
            
            
            
            