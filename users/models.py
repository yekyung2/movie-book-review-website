from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ Custom User Models"""

    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "eng"),
        (LANGUAGE_KOREAN, "kr"),
    )

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    GENRE_COMEDY = "comedy"
    GENRE_ROMANCE = "romance"
    GENRE_ACTION = "action"
    GENRE_SIFI = "sifi"
    GENRE_HORROR = "horror"

    GENRE_CHOICES = (
        (GENRE_COMEDY, "Comedy"),
        (GENRE_ROMANCE, "Romance"),
        (GENRE_ACTION, "Action"),
        (GENRE_SIFI, "Si-Fi"),
        (GENRE_HORROR, "Horror"),
    )

    bio = models.TextField(default="", blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=10, null=True, blank=True
    )

    favorite_book_genre = models.CharField(
        choices=GENRE_CHOICES, max_length=150, null=True, blank=True
    )

    favorite_movie_genre = models.CharField(
        choices=GENRE_CHOICES, max_length=150, null=True, blank=True
    )
