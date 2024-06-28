from rest_framework.response import Response
from rest_framework.decorators import api_view

from note.models import Note
from note.serializers import NoteSerializer


# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "endpoint": "notes",
            "method": "GET",
            "description": "Get all notes",
        },
        {
            "endpoint": "notes/create",
            "method": "POST",
            "description": "Add new note",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request, pk):
    res = f"Note {pk} deleted"
    note = Note.objects.get(id=pk)
    if note:
        note.delete()
        return Response(res)
    return Response("Note does not exist")
