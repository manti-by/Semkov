# Generated by Django 2.1.7 on 2019-05-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("pages", "0005_pagemodel_source_title")]

    operations = [
        migrations.AddField(
            model_name="pagemodel", name="map", field=models.TextField(blank=True)
        )
    ]
