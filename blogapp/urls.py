from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog_menu, name='blog_menu'),
    path('contact', views.contact, name='contact'),
    path('upload_blog', views.upload_blog, name='upload_blog'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('blog_like/<int:id>/', views.blog_like, name='blog_like'),
    path('blog_up/<int:id>/', views.blog_up, name='blog_up'),
    path('blog_down/<int:id>/', views.blog_down, name='blog_down'),
    path('priorityform/<int:id>/', views.priorityform, name='priorityform'),

    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('update_blog_cover/<int:pk>/', views.update_blog_cover, name='update_blog_cover'),

    path('bio_update', views.bio_update, name='bio_update'),
    path('mybio', views.mybio, name='mybio'),

    path('tags/<slug:tag_slug>/', views.TagIndexBlog, name='posts_by_tag'),
    path('blogsforuser/<int:id>/', views.blogsforuser, name='blogsforuser'),
    path('bioforuser/<int:id>/', views.bioforuser, name='bioforuser'),
    path('about_update', views.about_update, name='about_update'),
    path('site_about', views.site_about, name='site_about'),
    path('authormenu', views.authormenu, name='authormenu'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
