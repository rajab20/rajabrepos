from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=80)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blogs')
