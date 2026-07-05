from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # ModelSerializer derives the fields and validation from the Book model
    # itself (instead of declaring each field by hand like a plain
    # Serializer would), and it implements create()/update() out of the
    # box, converting between Book instances and JSON automatically.
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']
