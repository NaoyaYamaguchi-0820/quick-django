from django.contrib import admin
from .models import Book
from .models import Review
from .models import Author

# Register your models here.

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)