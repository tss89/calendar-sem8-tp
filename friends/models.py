from django.db import models

from calendar_sem8.settings import AUTH_USER_MODEL

class Friends(models.Model):

    facebook_id = models.CharField(max_length=150, db_index=True, blank=True, unique=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    email = models.CharField(max_length=100, default=None, null=True)
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)
    birth_date = models.DateField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
