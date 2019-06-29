from django.db import models
from django.urls import  reverse
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.utils.text import Truncator
from  django.utils import timezone
from markdown import markdown
# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=200 , unique=True)
    def __str__(self):
        return  self.slug


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body  = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    def publish(self):
        self.published_date = timezone.now()

        self.save()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("Entry_detail", kwargs= {"slug":self.slug})
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"

    def __str__(self):
        truncated_body = Truncator(self.body)
        return truncated_body.chars(30)

    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))

    ordering = ["created"]