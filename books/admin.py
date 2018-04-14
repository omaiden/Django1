from django.contrib import admin

# Register your models here.
from .models import Author, Publisher, Book

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)