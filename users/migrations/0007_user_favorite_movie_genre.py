# Generated by Django 2.2.5 on 2021-02-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_favorite_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_movie_genre',
            field=models.CharField(blank=True, choices=[('comedy', 'Comedy'), ('romance', 'Romance'), ('action', 'Action'), ('sifi', 'Si-Fi'), ('horror', 'Horror')], max_length=150, null=True),
        ),
    ]
