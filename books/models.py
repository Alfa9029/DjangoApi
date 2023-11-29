from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)