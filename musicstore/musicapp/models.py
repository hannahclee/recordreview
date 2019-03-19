from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table='name'

class Record(models.Model):
    recordtitle=models.CharField(max_length=255)
    recordrelease=models.DateField()
    artist=models.ManyToManyField(Artist)

    def __str__(self):
        return self.recordtitle

    class Meta:
        db_table='record'

class Review(models.Model):
    record=models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review=models.TextField()

    def __str__(self):
        return self.review
        
    class Meta:
        db_table='review'

