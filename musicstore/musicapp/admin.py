from django.contrib import admin
from .models import Artist, Record, Review

# Register your models here.
admin.site.register(Artist)
admin.site.register(Record)
admin.site.register(Review)