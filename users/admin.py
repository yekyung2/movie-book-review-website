from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = (
        "username",
        "language",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "language",
                    "preference",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                )
            },
        ),
    )

    list_filter = (
        "language",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
    )


fis