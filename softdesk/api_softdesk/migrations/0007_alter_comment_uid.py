# Generated by Django 4.2.3 on 2023-08-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_softdesk", "0006_comment_author_alter_comment_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="uid",
            field=models.CharField(
                default="dabe63cd-fdb4-4f98-bc87-a1c4d0458ad2", max_length=100
            ),
        ),
    ]
