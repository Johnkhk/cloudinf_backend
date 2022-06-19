from django.db import models

# class benlp()

# # Create your models here.
class Summarizer(models.Model):
    # context = models.CharField(max_length=50, default="", unique=True)
    context = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True)


