from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="get_routes"),
    path("notes", views.getNotes, name="get_notes"),
    path("note/<str:pk>", views.getNoteDetail, name="get_note_detail"),
    path("notes/create", views.createNote, name="create_note"),
    path("note/<str:pk>/update", views.updateNote, name="update_note"),
    path("note/<str:pk>/delete", views.deleteNote, name="delete_note"),
]
