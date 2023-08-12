from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField('Title', max_length=200, )
    content = models.TextField('Write a note')
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()
    author = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, related_name='notes',)
    slug = models.SlugField(editable=False)
    # contributors = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        self.slug = slugify(self.title)
        return super(Note, self).save(*args, **kwargs)
