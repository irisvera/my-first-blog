from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

def publish(self):
    sel.published_date = timezone.now()
    self.save()

def _str_(self):
    return self.title

# Create your models here.
