from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Review(models.Model):
    NULL = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = (
        (NULL, 0),
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
    )
    title = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    review = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating = models.IntegerField(choices=RATING_CHOICES, default=ONE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reviews')
