from django.db import models

# Create your models here.


class Urls(models.Model):
    link = models.CharField(max_length=16300)
    uuid = models.CharField(max_length=20)
    click_count = models.IntegerField(default=0)
    last_clicked = models.DateTimeField(null=True)

