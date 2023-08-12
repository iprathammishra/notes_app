from django.contrib.auth.models import User
from rest_framework import serializers

from notes.models import Note, Label


class NoteSerializer(serializers.ModelSerializer):
    """
Serializing all the Notes
"""

    class Meta:
        model = Note
        fields = ('id', 'author', 'title', 'content', 'labels', 'created', 'updated')


class LabelSerializer(serializers.ModelSerializer):
    """
Serializing all the Notes
"""
    notes = NoteSerializer(read_only=True, many=True, source="note_set")

    class Meta:
        model = Label
        fields = ('id', 'user', 'name', 'notes')


class AuthorSerializer(serializers.ModelSerializer):
    """
Serializing all the Authors
"""
    notes = NoteSerializer(read_only=False, many=True, source="note_set")

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'username', 'notes')
