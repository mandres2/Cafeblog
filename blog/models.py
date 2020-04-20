from django.db import models
from django.utils import timezone
# One to many relationship
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #Reverse Function return form URL as a string and let view handle re-direct
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
