from django.test import TestCase

from library.models import Article, Book


class ArticleListViewTests(TestCase):
    def test_displays_articles_from_the_database(self):
        Article.objects.create(
            name="First article",
            link="https://example.com/first",
            annotation="A useful summary.",
        )
        Article.objects.create(
            name="Second article",
            link="https://example.com/second",
            annotation="Another summary.",
            status=Article.Status.FINISHED,
        )

        response = self.client.get("/articles/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First article")
        self.assertContains(response, "https://example.com/first")
        self.assertContains(response, "A useful summary.")
        self.assertContains(response, "Second article")
        self.assertContains(response, "https://example.com/second")
        self.assertContains(response, "Another summary.")
        self.assertContains(response, "finished")

    def test_displays_empty_state_when_there_are_no_articles(self):
        response = self.client.get("/articles/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles yet.")


class ArticleCreateViewTests(TestCase):
    def test_renders_form_with_csrf_token(self):
        response = self.client.get("/articles/add/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="link"')
        self.assertContains(response, 'name="annotation"')
        self.assertContains(response, 'name="status"')

    def test_saves_article_and_redirects_to_article_list(self):
        response = self.client.post(
            "/articles/add/",
            data={
                "name": "New article",
                "link": "https://example.com/new",
                "annotation": "A useful summary.",
            },
        )

        self.assertRedirects(response, "/articles/")
        self.assertTrue(
            Article.objects.filter(
                name="New article",
                link="https://example.com/new",
                annotation="A useful summary.",
                status=Article.Status.NEW,
            ).exists()
        )


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
