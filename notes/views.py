from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, UpdateView

from notes.models import Note


# Create your views here.
def home_page(request):
    notes = Note.objects.get(user=request.user)
    return render(request, 'notes/index.html', context={
        'notes': notes,
    })


def new_note(request, **kwargs):
    # form = NoteForm(request.POST)
    # if form.is_valid:
    note = Note(
        title=request.POST['title'],
        content=request.POST['content'],
        updated=request.POST['updated'],
        user=request.user,
        labels=request.POST['labels']
    )
    note.save()


