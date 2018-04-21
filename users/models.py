from django.contrib.auth.models import AbstractUser
from django.db import models

class CalendarUser(AbstractUser):

    facebook_id = models.CharField(max_length=150, db_index=True, blank=True)
