# Generated by Django 4.2.1 on 2023-05-29 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_post_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
    ]
