from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db.models import Count, Min, Sum, Avg
from django.core.validators import MaxValueValidator, MinValueValidator

from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    bio = RichTextUploadingField(max_length=50000, blank=True)
    location = models.CharField(max_length=30, blank=True)
#    birth_date = models.DateField(null=True, blank=True)
    visit_num = models.PositiveIntegerField(default=0)
    like_num = models.PositiveIntegerField(default=0)
    profilepicture = models.ImageField(upload_to='profilepicture', default="profilepicture/profilepicture.png")

    def __str__(self):
        return self.user


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)
#    priority = models.PositiveIntegerField()
#    priority = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999),],)
    title = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
#    letter = models.CharField(max_length=20000, blank=True)
    letter = RichTextUploadingField(max_length=50000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    visit_num = models.PositiveIntegerField(default=0)
    like_num = models.PositiveIntegerField(default=0)
    coverpicture = models.ImageField(upload_to='aboutcover', default="default.jpg")
#    location = models.CharField(max_length=50)
#    date = models.DateTimeField(null='True')
#    aboutpicture = models.ImageField(upload_to='aboutpicture')

    def __str__(self):
        return self.title

#    def obj_count(self):
#        count = self.title.count
#        return count

# To also delete the document & image itself in the files:
    def delete(self, *args, **kwargs):
#        self.document.delete()
#        self.aboutpicture.delete()
        self.coverpicture.delete()
        super().delete(*args, **kwargs)

    def datepublished(self):
        return self.pub_date.strftime('%B %d %Y')

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentlist', null='True')
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400, blank=True)
    time = models.DateTimeField(auto_now_add=True)
#    like_num = models.PositiveIntegerField(default=0, blank=True, null='True')
	
    def __str__(self):
        return self.comment


class About(models.Model):
    letter = RichTextUploadingField(max_length=50000, blank=True)