# Generated by Django 4.2.3 on 2023-08-23 16:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api_softdesk", "0003_issue"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="contributor", unique_together={("project", "user")},
        ),
    ]
