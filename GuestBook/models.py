from django.db import models
import datetime

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    create_date = models.DateTimeField(default=datetime.datetime.now)