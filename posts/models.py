from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)
    pinned = models.BooleanField()
    
    def __str__(self):
        return self.title