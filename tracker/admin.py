from django.contrib import admin

from .models import Expense, Tag

# Register your models here.
admin.site.register(Expense)
admin.site.register(Tag)
