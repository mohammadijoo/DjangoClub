from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django_comments_xtd.models import XtdComment
from django.utils.text import slugify


#from wagtail.wagtailcore.models import Page
#from wagtail.core.models import Page
# from wagtail.wagtailcore.fields import StreamField

# from wagtail.wagtailcore import blocks
# from wagtail.wagtailimages.blocks import ImageChooserBlock
# from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
# from wagtail.wagtailsnippets.models import register_snippet

# from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
#from modelcluster.fields import ParentalKey

# from .views import ArticleDetailView



class Category(models.Model):
    name = models.CharField(max_length=255)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('theblog')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    phone = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    hobby = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    stackoverflow_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.user)
        
    def get_absolute_url(self):
        return reverse('theblog')
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="Django Club's Blog")
    meta_tag = models.CharField(max_length=255, default="Django")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default="Python")
    snippet = models.CharField(max_length=1000)
    publish = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    slug = models.SlugField(null=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
        
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id))) 
        return reverse('theblog')
        #return reverse('theblog', kwargs={"slug": self.slug})
        #return reverse('article_detail', kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-post_date']
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        
        
# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.name)


# class ArticlePage(Page):
#     template = 'theblog/article_details.html'


# class CustomComment(XtdComment):
#     page = ParentalKey(Post, on_delete=models.CASCADE, related_name='customcomments')
    
#     def save(self, *args, **kwargs):
#         self.user_name = self.user.display_name
#         self.page = Post.objects.get(pk=self.object_pk)
#         super(CustomComment, self).save(*args, **kwargs)















