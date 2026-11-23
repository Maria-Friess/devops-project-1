from django.test import TestCase

from library.models import Article, Book


class ArticleListViewTests(TestCase):
    def test_displays_articles_from_the_database(self):
        first_article = Article.objects.create(
            name="First article",
            link="https://example.com/first",
            annotation="A useful summary.",
            source="Example publisher",
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
        self.assertContains(response, "Example publisher")
        self.assertContains(response, "Second article")
        self.assertContains(response, "https://example.com/second")
        self.assertContains(response, "Another summary.")
        self.assertContains(response, "finished")
        self.assertContains(response, f'href="/articles/{first_article.pk}/edit/"')

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
        self.assertContains(response, 'name="source"')
        self.assertContains(response, 'name="status"')

    def test_saves_article_and_redirects_to_article_list(self):
        response = self.client.post(
            "/articles/add/",
            data={
                "name": "New article",
                "link": "https://example.com/new",
                "annotation": "A useful summary.",
                "source": "Example publisher",
            },
        )

        self.assertRedirects(response, "/articles/")
        self.assertTrue(
            Article.objects.filter(
                name="New article",
                link="https://example.com/new",
                annotation="A useful summary.",
                source="Example publisher",
                status=Article.Status.NEW,
            ).exists()
        )


class ArticleEditViewTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            name="Existing article",
            link="https://example.com/existing",
            annotation="Original annotation",
            source="Original source",
        )

    def test_displays_existing_article_in_form(self):
        response = self.client.get(f"/articles/{self.article.pk}/edit/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        self.assertContains(response, 'value="Existing article"')
        self.assertContains(response, 'value="https://example.com/existing"')

    def test_updates_article_and_redirects_to_article_list(self):
        response = self.client.post(
            f"/articles/{self.article.pk}/edit/",
            data={
                "name": "Updated article",
                "link": "https://example.com/updated",
                "annotation": "Updated annotation",
                "source": "Updated source",
                "status": Article.Status.FINISHED,
            },
        )

        self.assertRedirects(response, "/articles/")
        self.article.refresh_from_db()
        self.assertEqual(self.article.name, "Updated article")
        self.assertEqual(self.article.link, "https://example.com/updated")
        self.assertEqual(self.article.annotation, "Updated annotation")
        self.assertEqual(self.article.source, "Updated source")
        self.assertEqual(self.article.status, Article.Status.FINISHED)


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
