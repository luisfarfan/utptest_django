from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, action
from notes.models import Notes
from notes.serializer import NotesSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

    @list_route(methods=['get'], url_path='by_user/(?P<user_id>[0-9]+)')
    def notes_by_user(self, request, user_id):
        queryset = Notes.objects.filter(user_id=user_id)
        response = self.serializer_class(many=True, instance=queryset).data
        return Response(response)
