from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.forms import ArticleForm
from library.models import Article, Book
from library.serializers import BookSerializer


def article_list(request):
    articles = Article.objects.all()
    return render(request, "library/article_list.html", {"articles": articles})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article-list")
    else:
        form = ArticleForm()

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
