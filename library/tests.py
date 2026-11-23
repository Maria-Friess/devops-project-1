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


class BookCreateViewTests(TestCase):
    def test_creates_book_from_post_request(self):
        response = self.client.post(
            "/book/",
            data={"name": "New article", "annotation": "A useful summary."},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "New article")
        self.assertEqual(response.json()["annotation"], "A useful summary.")
        self.assertTrue(
            Book.objects.filter(name="New article", annotation="A useful summary.").exists()
        )
