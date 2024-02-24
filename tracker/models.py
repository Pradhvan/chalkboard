from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField


class TagManager(models.Manager):
    def get_or_create_tags(self, tag_names):
        tags = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = self.get_or_create(name=tag_name)
                tags.append(tag)
        return tags


class Tag(models.Model):
    name = models.CharField(max_length=50)

    objects = TagManager()

    def __str__(self):
        return self.name


RECURRING_CHOICES = [
    ("none", "None"),
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
    ("yearly", "Yearly"),
]


class Expense(models.Model):
    amount = MoneyField(max_digits=7, decimal_places=2, default_currency="INR")
    recurring = models.CharField(
        max_length=10, choices=RECURRING_CHOICES, default="none"
    )
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
