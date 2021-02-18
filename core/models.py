from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        abstract = True