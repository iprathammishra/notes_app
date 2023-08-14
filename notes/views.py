from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView, UpdateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from notes.models import Note
from notes.serializers import NoteSerializer


# Create your views here.


@api_view(['GET'])
def home_page(request):
    # notes = Note.objects.all()
    notes_by_author = Note.objects.filter(author_id=request.user.id)
    if request.method == 'GET':
        serializer = NoteSerializer(notes_by_author, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        note = JSONParser().parse(request)
        tutorial_serializer = NoteSerializer(data=note)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def delete_edit_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        note.delete()
        return Response({'message': 'Note was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_note(request, slug):
    try:
        note = Note.objects.filter(author_id=request.user.id).get(slug=slug)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

