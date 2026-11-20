from django.test import TestCase

from library.models import Book


class ArticleListViewTests(TestCase):
    def test_displays_articles_from_the_database(self):
        Book.objects.create(name="First article", annotation="A useful summary.")
        Book.objects.create(name="Second article", annotation="Another summary.")

        response = self.client.get("/articles/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First article")
        self.assertContains(response, "A useful summary.")
        self.assertContains(response, "Second article")
        self.assertContains(response, "Another summary.")

    def test_displays_empty_state_when_there_are_no_articles(self):
        response = self.client.get("/articles/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles yet.")
