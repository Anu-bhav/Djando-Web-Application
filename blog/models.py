from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Don't put parenthesis timezone.now() as we do not want it to be executed at that point
    # we just want to pass the function name as the default value so that it knows what to execute later
    date_posted = models.DateTimeField(default=timezone.now)
    # when a user is deleted, the post associated to that user will be deleted too with on_delete=models.CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # for django to find the location of a post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})