from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.forms import BookForm
from library.models import Book
from library.serializers import BookSerializer


def article_list(request):
    return render(request, "library/article_list.html", {"articles": Book.objects.all()})


def article_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article-list")
    else:
        form = BookForm()

    return render(request, "library/article_form.html", {"form": form})


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
