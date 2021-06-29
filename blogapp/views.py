from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib import messages
#from django.db.models import Sum
import os
#from django.contrib.auth.models import User

from .models import *
from .forms import *

#FOR CONTACT VIEW:
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils.datastructures import MultiValueDictKeyError

# FOR Translate:
from django.utils.translation import gettext as _

# FOR BLOG TAGS:
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from django.db.models import Count

def blog_menu(request):
    blogs = Blog.objects.all().order_by('priority')
#    users = User.objects.all()
    tags = Tag.objects.all()
#    tags = Tag.objects.annotate(Count('blog')
    blognum = User.objects.filter(is_staff=True).annotate(total_posts = Count('blog'))

    return render(request, 'blog_menu.html', {'blogs':blogs, 'tags':tags, 'blognum':blognum})

def blogsforuser(request, id):
    blogs = Blog.objects.filter(user_id=id).order_by('priority')
    tags = Tag.objects.all()
    blognum = User.objects.filter(is_staff=True).annotate(total_posts = Count('blog'))

    return render(request, 'blog_menu.html', {'blogs':blogs, 'tags':tags, 'blognum':blognum})

def bioforuser(request, id):
    mybio, created = Profile.objects.get_or_create(user_id=id)

    blogs = Blog.objects.filter(user_id=id).order_by('priority')
    return render(request, 'bio.html', {'blogs':blogs, 'mybio':mybio})

def TagIndexBlog(request, tag_slug):
    tags = Tag.objects.all()
    blogs = Blog.objects.filter(tags__slug=tag_slug).order_by('priority')
    blognum = User.objects.filter(is_staff=True).annotate(total_posts = Count('blog'))

    return render(request, 'blog_menu.html', {'blogs':blogs, 'tags':tags, 'blognum':blognum})



def bio_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been updated.')
            return redirect('profile_update')
    else:
        form = ProfileForm(instance=request.user)
        
    return render(request, 'update_blog.html', {'form':ProfileForm(instance=profile)})

def mybio(request):
    mybio, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'bio.html', {'mybio':mybio})


def authormenu(request):
    authors = User.objects.filter(is_staff=True).annotate(total_posts = Count('blog'))
    return render(request, 'author_menu.html', {'authors':authors})



def about_update(request):
    about, created = About.objects.get_or_create(id=1)
    form = AboutForm(instance=about)

    if request.user.username == 'admin':
        if request.method == 'POST':
            form = AboutForm(request.POST, instance=about)
            if form.is_valid():
                form.save()
                messages.info(request, 'You\'ve updated about letter of the site.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                form = AboutForm(instance=about)
                messages.error(request, 'Something went wrong')
        return render(request, 'update_blog.html', {'form':form})
    else:
        return HttpResponse('Please sign in with admin account')


def site_about(request):
    about = About.objects.get(id=1)
    return render(request, 'about_letter.html', {'about':about})

#def Blog(request, id):
#    bloglist = Blog.objects.filter(id=id)
#    ls = Blog.objects.get(id=id)

    "#Number of visits to this view, as counted in the session variable."
#    num_visits = request.session.get('num_visits', 0)
#    request.session['num_visits'] = num_visits + 1
#    return render(request, 'blog.html', {'bloglist':bloglist, 'ls':ls, 'num_visits': num_visits})
# Put this in blog html file --> Visitors: {{ num_visits }}

def blog(request, id):
    bloglist = Blog.objects.filter(id=id)
    ls = Blog.objects.get(id=id)

    # To Add Visit Number
    ls.visit_num += 1
    ls.save()
    
    # For Add Chat and Chat Form
    if request.method == 'POST':
        form = BlogChatForm(request.POST)
        if form.is_valid():
            newchat = ls.chat_set.create(comment=form.cleaned_data['comment'])
            newchat.save()
            request.user.commentlist.add(newchat)
            ls.visit_num -= 2
            ls.save()
        return redirect('blog', id=id)
    else:
        form = BlogChatForm()
        priority_form = BlogPriorityForm(request.POST, instance=ls)
        blog_count = (Blog.objects.count()-1)
    return render(request, 'blog.html', {'bloglist':bloglist, 'ls':ls, 'form':form, 'priority_form':BlogPriorityForm(instance=ls), 'blog_count':blog_count})







def priorityform(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        new_form = BlogPriorityForm(request.POST)
#        if new_form.is_valid():
        if request.POST.get('priorityinput'):
#            blog.priority = request.POST.get('priorityinput')
#            blog.save()
            # IF NEW PRIORITY VALUE IS LESS THAN PREVIOUS PRIORITY (BELOW FUNTION IS BEING USED IF NEW PRIORITY IS LESS THAN PREVIOUS/CURRENT PRIORITY):
            #if blog.priority > new_form.cleaned_data['priority']:
            if str(blog.priority) > request.POST.get('priorityinput'):
                # Below is increasing prioritiy number of all objects whose priority number is smaller than previous priority of updated object.
                for blogi in Blog.objects.filter(priority__lte=blog.priority):
                    blogi.priority += 1
                    blogi.save()
                # below is updating priority of the object from the form:
                #blog.priority = new_form.cleaned_data['priority']
                blog.priority = request.POST.get('priorityinput')
                blog.save()
                # Above 'for blogs in Blog.objects.filter(priority__lte=blog.priority):' funtion also increases priority of objects whose priority are smaller than priority of updated object. so we are decreasing priority of those objects (whose priority are smaller than priority of updated object) with below function back.
                for blogii in Blog.objects.filter(priority__lte=blog.priority):
                    blogii.priority -= 1
                    blogii.save()
                # below is updating priority of the object from the form:    
                #blog.priority = new_form.cleaned_data['priority']
                blog.priority = request.POST.get('priorityinput')
                blog.save()


            # IF NEW PRIORITY VALUE IS GREATER THAN PREVIOUS PRIORITY (BELOW FUNTION IS BEING USED IF NEW PRIORITY IS GREATER THAN PREVIOUS/CURRENT PRIORITY):
            if str(blog.priority) < request.POST.get('priorityinput'):
                # If current/previous number is '0' than it gives error because below 'for blogn in Blog.objects.filter(priority__gte=blog.priority):' functon can not find objects whose priorities are smaller than '0' so we are adding 1 to current prioriy in formula and it is being 'for blogn in Blog.objects.filter(priority__gte=(blog.priority+1)):' so if current formula is '0' the formula checks objects whose priority is smaller than 1 and could find itself at least and does not give error. (I THINK WE COULD SOLVE THIS PROBLE ADDING TYPE AND MIN VALUES TO OUR BFORM BUTTON LIKE: '<button type="submit" type="number" min="0.0">Ok</button>' so I disabled below:)
#                if blog.priority==0:
                    # Below is decreasing prioritiy number of all objects whose priority number is greater than previous priority of updated object.
#                    for blogd in Blog.objects.filter(priority__gte=(blog.priority+1)):
#                        blogd.priority -= 1
#                        blogd.save()
                    # below is updating priority of the object from the form:
#                    blog.priority = new_form.cleaned_data['priority']
#                    blog.save()
                    # Above 'for blogd in Blog.objects.filter(priority__gte=(blog.priority+1)):' funtion also decreases priority of objects whose priority are greater than priority of updated object. so we are increasing priority of those objects (whose priority are greater than priority of updated object) with below function back.
#                    for blogdd in Blog.objects.filter(priority__gte=blog.priority):
#                        blogdd.priority += 1
#                        blogdd.save()
                    # below is updating priority of the object from the form:
#                    blog.priority = new_form.cleaned_data['priority']
#                    blog.save()
                # If current/previous number is not '0' we can use 'for blogd in Blog.objects.filter(priority__gte=blog.priority):' without adding 1 to blog.priority like '(priority__gte=(blog.priority+1)):' as below:
#                else:
                    # Below is decreasing prioritiy number of all objects whose priority number is greater than previous priority of updated object.
                for blogd in Blog.objects.filter(priority__gte=blog.priority):
                    blogd.priority -= 1
                    blogd.save()
                # below is updating priority of the object from the form:
                blog.priority = request.POST.get('priorityinput')
                blog.save()
                # Above 'for blogd in Blog.objects.filter(priority__gte=blog.priority):' funtion also decreases priority of objects whose priority are greater than priority of updated object. so we are increasing priority of those objects (whose priority are greater than priority of updated object) with below function back.
                for blogdd in Blog.objects.filter(priority__gte=blog.priority):
                    blogdd.priority += 1
                    blogdd.save()
                # below is updating priority of the object from the form:
                blog.priority = request.POST.get('priorityinput')
                blog.save()
                
            

            return redirect('blog', id=id)
    

def blog_like(request, id):
    blogletter = Blog.objects.get(id=id)
    blogletter.like_num += 1
    blogletter.visit_num -= 1
    blogletter.save()
    
    return redirect('blog', id=id)

#def blog_chat_like(request, id):
#    blog = Blog.objects.get(id=id)


def upload_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            sa = form.save(commit=False)
            sa.user = request.user
            # Below insert priority of blog number of blogs in model.
            sa.priority = Blog.objects.count()
            sa.save()
            return redirect('upload_blog')
    else:
        form = BlogForm()
    return render(request, 'update_blog.html', {'form':form})


def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    # Beow function increase priority number of each object which is greater than 'pk' number.
    # priority__gte=5 filters bigger than or equal 5
    # priority__lte=5 filters smaller than or equal 5
    for blogs in Blog.objects.filter(priority__gte=blog.priority):
        blogs.priority -= 1
        blogs.save()

    # remove_all_tags_without_objects
    for tag in Tag.objects.all():
        if tag.taggit_taggeditem_items.count() == 0:
            # print('Removing: {}'.format(tag))
            tag.delete()
        else:
            # print('Keeping: {}'.format(tag))
            pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def blog_up(request, id):
    blog = Blog.objects.get(id=id)
    
    if blog.priority<=0:
       return redirect('blog_menu')
    else:
        blog_d = Blog.objects.get(priority = (blog.priority-1))
        blog_d.priority += 1
        blog_d.save()

        blog.priority -= 1
        blog.save()
        return redirect('blog_menu')

def blog_down(request, id):
    blog = Blog.objects.get(id=id)

    try:
        blog_d = Blog.objects.get(priority = (blog.priority+1))
        blog_d.priority -= 1
        blog_d.save()

        blog.priority += 1
        blog.save()
        return redirect('blog_menu')
    except:
        return redirect('blog_menu')


def update_blog(request, id):
    blogp = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogp)
        if form.is_valid():
            form.save()
        return redirect('update_blog', id=id)
    else:
        return render(request, 'update_blog.html', {'form':BlogForm(instance=blogp)})

def update_blog_cover(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogCoverUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            # TO DELETE blog COVER PICTURE:
            blog.coverpicture.delete()
			# TO UPLOAD blog COVER PICTURE:
            blog = Blog.objects.get(pk=pk)
            blog.coverpicture = form.cleaned_data['coverpicture']
            blog.save()
            return redirect('blog_menu')
    else:
        form = BlogCoverUpdateForm()
    return render(request, 'update_blog_cover.html', {'form':form})







def contact(request):
    if request.method == 'GET':
        form = ContactForm(request.POST, request.FILES)
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = 'Blog Contact Form'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            message= str(name) + " with the email, " + str(email) + ", sent the following message:\n\n" + str(text);

            email = EmailMessage(subject, message, 'codenotes.py@gmail.com', ['codenotes.py@gmail.com'])
            email.content_subtype = 'html'
            
            # IF THERE IS ATTACHMENT:
            try:
                for f in request.FILES.getlist('file'):
                    email.attach(f.name, f.read(), f.content_type)
                email.send()
            # IF THERE IS NOT ANY ATTACHMENT:
            except MultiValueDictKeyError:
                file = False
                email.send()

            return redirect('contact')
    return render(request, "contact.html", {'form': form})

