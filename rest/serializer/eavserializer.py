from rest_framework import serializers
from rest.models.eav_typed_column import Entity, Attribute, Value


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ["id", "name"]


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["id", "name", "attribute_type"]


class ValueSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Value
        fields = ["id", "value", "entity", "attribute"]

    def get_value(self, obj):
        return obj.value
