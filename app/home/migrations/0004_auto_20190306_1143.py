# Generated by Django 2.1.7 on 2019-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0003_homepagemodel_menu_title")]

    operations = [
        migrations.AddField(
            model_name="categorymodel",
            name="homepage_title",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="categorymodel",
            name="is_homepage",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="homepagemodel",
            name="homepage_title",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="homepagemodel",
            name="is_homepage",
            field=models.BooleanField(default=False),
        ),
    ]
