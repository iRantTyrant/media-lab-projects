#Import the models module so we can create our models
from django.db import models
#Import the settings module so we can use the AUTH_USER_MODEL setting
from django.conf import settings
#Import the module so we can use the reverse function for the SEO friendly urls
from django.urls import reverse
#Import the tags module so we can use add and remove tags from posts
from taggit.managers import TaggableManager

#Create a model for the blog posts
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'P', 'Published'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['publish']

    def __str__(self):
        return self.title
    def get_absolute_url(self): #This function returns the url of the post based on the publish date and the slug
        return reverse('blogapp:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
    ])
    tags = TaggableManager() #This enables us to add tags to the posts
#Create a model for the blog posts 

#Create a model for the comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
