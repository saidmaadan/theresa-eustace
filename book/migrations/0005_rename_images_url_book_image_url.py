# Generated by Django 5.0.6 on 2024-05-31 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_images_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='images_url',
            new_name='image_url',
        ),
    ]
