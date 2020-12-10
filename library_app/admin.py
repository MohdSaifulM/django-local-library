from django.contrib import admin
from .models import *

# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id", "branch")

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_borrowed", "borrower", "branch", "available")


admin.site.register(Library, LibraryAdmin)
admin.site.register(Book, BookAdmin)
