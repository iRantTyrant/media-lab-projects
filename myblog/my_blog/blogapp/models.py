from django.db import models
from django.conf import settings
from django.urls import reverse

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
    def get_absolute_url(self):
        return reverse('blogapp:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
    ])
