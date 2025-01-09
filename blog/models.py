from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True, null=True)  # URL for image (or you can use FileField)
    excerpt = models.CharField(max_length=255, blank=True, null=True)  # Short excerpt for the blog post
    category = models.CharField(max_length=100, blank=True, null=True)  # Optional category

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return "Contact Information"

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)  # Optional photo for the team member

    def __str__(self):
        return self.name