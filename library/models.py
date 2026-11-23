from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    annotation = models.TextField()


class Article(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        FINISHED = "finished", "Finished"
        REREAD = "reread", "Reread"

    name = models.CharField(max_length=100)
    link = models.URLField(max_length=400)
    annotation = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.NEW,
    )
    