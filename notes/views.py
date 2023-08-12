from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView, UpdateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notes.models import Note
from notes.serializers import NoteSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def home_page(request):
    notes = Note.objects.get(author=request.user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_edit_note(request, **kwargs):
    if request.method == 'GET':
        return render('notes/new_note.html', request)
    elif request.method == 'POST':
        data = {'text': request.DATA.get('note'), 'author': request.user}
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_note(request, **kwargs):
    note = Note.objects.filter(author=request.user).get(slug=slugify(kwargs['title']))
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
