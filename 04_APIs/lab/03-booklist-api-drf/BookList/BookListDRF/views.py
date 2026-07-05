from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookView(generics.ListCreateAPIView):
    # ListCreateAPIView bundles "list all" (GET) and "create" (POST) for a
    # collection endpoint, so /books supports both without writing get()/
    # post() by hand -- chosen because the collection only ever needs to
    # be listed and appended to, never updated or deleted as a whole.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    # RetrieveUpdateAPIView bundles "fetch one" (GET) and "update" (PUT/
    # PATCH) for a single resource, matching the /books/<pk> endpoint --
    # DestroyAPIView is deliberately left out of the inheritance here, so
    # this endpoint does not support DELETE.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
