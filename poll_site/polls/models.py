import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True, verbose_name ='ID')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    opened = models.BooleanField(default=True)
    # Helpful representation of the text of object
    def __str__(self):
        return self.question_text

    # A custom method for finding recent posts
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
