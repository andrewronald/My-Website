from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField()
    post_text = models.TextField()
    post_title = models.CharField(max_length = 50)
    