# Generated by Django 4.2 on 2023-05-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_remove_blog_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
