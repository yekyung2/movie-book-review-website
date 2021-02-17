from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ Custom User Models"""

    # PREFERENCE_BOOKS = "books"
    # PREFERENCE_MOVIES = "movies"

    # PREFERENCE_CHOICES = (
    #     (PREFERENCE_BOOKS, "Books"),
    #     (PREFERENCE_MOVIES, "Movies"),
    # )

    # LANGUAGE_ENGLISH = "en"
    # LANGUAGE_KOREAN = "ko"

    # LANGUAGE_CHOICES = (
    #     (LANGUAGE_ENGLISH, "English"),
    #     (LANGUAGE_KOREAN, "Korean"),
    # )

    # bio = models.TextField(default="")
    # preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=150)
    # language = models.CharField(choices=LANGUAGE_CHOICES, max_length=150)

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

    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
