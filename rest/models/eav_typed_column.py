# example of typed column approach
from django.db import models

from django.contrib.auth import get_user_model


class Entity(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "user"], name="unique_entity_per_user"
            )
        ]


class Attribute(models.Model):
    name = models.CharField(max_length=64)
    attribute_type = models.CharField(max_length=100)


class Value(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    text_value = models.CharField(max_length=255, null=True)
    integer_value = models.IntegerField(null=True)
    float_value = models.FloatField(null=True)
    date_value = models.DateTimeField(null=True)
    boolean_value = models.BooleanField(null=True)

    @property
    def value(self):
        if self.attribute.attribute_type == "text":
            return self.text_value
        if self.attribute.attribute_type == "integer":
            return self.integer_value
        if self.attribute.attribute_type == "float":
            return self.float_value
        if self.attribute.attribute_type == "date":
            return self.date_value
        if self.attribute.attribute_type == "boolean":
            return self.boolean_value
        raise None
