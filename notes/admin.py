from django.contrib import admin

from notes.models import Note, Label

# Register your models here.
admin.site.register(Note)
admin.site.register(Label)
