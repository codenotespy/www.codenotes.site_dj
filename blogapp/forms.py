from django import forms
from .models import *
from django.forms import ClearableFileInput

#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('bio', 'title', 'location', 'profilepicture')

class BlogForm(forms.ModelForm):
#    aboutpicture = forms.ImageField(widget=forms.FileInput(attrs={'multiple':'multiple'}))

    class Meta:
        model = Blog
        fields = ('title', 'tags', 'coverpicture', 'letter', 'title_tr', 'letter_tr',)
        widgets = {
            'title': forms.Textarea(attrs={'style':'height:1.5rem; width:30rem;'}),
            'letter': RichTextField(),
            'title_tr': forms.Textarea(attrs={'style':'height:1.5rem; width:30rem;'}),
            'letter_tr': RichTextField(),
        }
        labels = {"title": "Title(en)", "letter": "Letter(en)"}

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('letter',)
        widgets = {
            'letter': RichTextField(),
#            'letter_tr': RichTextField(),
        }
#        labels = {"letter": "Letter(en)"}

# FOR Chat FORM
class BlogPriorityForm(forms.ModelForm):
#    priority = forms.IntegerField(label="priority")
#    priority = forms.IntegerField(label="priority", widget=forms.IntegerField(attrs={'min':0, 'max':'5', 'type':'number'}))    
    class Meta:
        model = Blog
#        obj_count = model.objects.count()
        fields = ('priority',)
#        widgets = {'priority': forms.TextInput(attrs={'min':0, 'max':obj_count, 'type':'number'})}
        widgets = {'priority': forms.TextInput(attrs={'min':0, 'type':'number'})}
        labels = {"priority": "Priority"}


# UPDATE FORM FOR Blog COVER PICTURE:
class BlogCoverUpdateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('coverpicture',)


# FOR Chat FORM
class BlogChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('comment',)
        widgets = {'comment': forms.Textarea(attrs={'placeholder':'Yorumunuz..', 'style':'height:5rem; width:100%; text-align:left; opacity:0.8;'})}
        labels = {"comment": ""}


# FOR CONTACT FORM
class ContactForm(forms.Form):
#    from_email = forms.EmailField(required=True)
#    subject = forms.CharField(required=True)
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=False)
