from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200, )
    content = models.TextField()
    created = models.DateTimeField(auto_created=timezone.now(), editable=False)
    updated = models.DateTimeField()
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Note, self).save(*args, **kwargs)
