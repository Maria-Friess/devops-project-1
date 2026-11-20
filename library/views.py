from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from library.models import Book
from library.serializers import BookSerializer


def article_list(request):
    return render(request, "library/article_list.html", {"articles": Book.objects.all()})


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
