from django.contrib import admin
from django.db import models
from django.forms import TextInput
from book.models import Book

class BookAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
        models.CharField: {'widget': TextInput(attrs={'size':'70'})},
        }

admin.site.register(Book,BookAdmin)

