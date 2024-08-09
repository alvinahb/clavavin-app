from django.db import models


# Date fields used in models
class DateFields:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Wine model
class Wine(models.Model, DateFields):
    name = models.CharField(max_length=32, null=False)
    domain = models.CharField(max_length=32, null=True)
    year = models.IntegerField(null=False)
    appellation = models.CharField(max_length=32, null=True)

    def __str__(self):
        return ' - '.join((self.name, self.year))
