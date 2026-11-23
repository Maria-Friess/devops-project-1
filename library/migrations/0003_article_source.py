from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="source",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
