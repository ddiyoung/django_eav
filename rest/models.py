from django.db import models
from django.db.models.fields import Field
# Create your models here.

DJANGO_FIELD_TYPES = [(cls.__name__, cls.__name__) for cls in Field.__subclasses__()]

class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Column(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(max_length=255)
    column_type = models.CharField(max_length=50, choices=DJANGO_FIELD_TYPES)
    is_nullable = models.BooleanField(default=True)

    def __str__(self):
        return f"table : {self.table.name}, column : {self.name}"