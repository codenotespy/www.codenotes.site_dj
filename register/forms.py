from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User





# REGISTER FORM
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        # make fields required if desired
#        email = forms.EmailField(required=True)
#        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        fields = ['username', 'first_name' , 'last_name', 'email', 'password1', 'password2', 'is_staff']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email')
        help_texts = {
            'username': None,
        }





###  ###   ###   ###   ###   ###   ###
### TO CREATE CUSTOM USER FORM ###
###  ###   ###   ###   ###   ###   ###
# FOR USER FORM
#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User


# FOR USER FORM
#class UserCreateForm(UserCreationForm):

#    class Meta:
#        model = User
        # make fields required if desired
#        first_name = forms.CharField(required=True)
#        last_name = forms.CharField(required=True)
#        email = forms.EmailField(required=True)
#        fields = ('username', 'first_name' , 'last_name', 'email', 'password1', 'password2',)

#class UserAdmin(UserAdmin):
#    add_form = UserCreateForm
#    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
#        }),
#    )
# Re-register UserAdmin
#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
###  ###   ###   ###   ###   ###   ###
###                            ###
###  ###   ###   ###   ###   ###   ###

