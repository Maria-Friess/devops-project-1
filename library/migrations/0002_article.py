from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("link", models.URLField(max_length=400)),
                ("annotation", models.CharField(blank=True, max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("finished", "Finished"),
                            ("reread", "Reread"),
                        ],
                        default="new",
                        max_length=8,
                    ),
                ),
            ],
        ),
    ]
