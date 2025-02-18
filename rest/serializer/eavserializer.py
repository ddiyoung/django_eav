from rest_framework import serializers
from rest.models.eav_typed_column import Entity, Attribute, Value


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ["name"]


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["name", "attribute_type"]


class ValueSerializer(serializers.ModelSerializer):
    value = serializers.CharField(required=True)
    attribute = AttributeSerializer(required=True)
    entity = EntitySerializer(required=True)

    class Meta:
        model = Value
        fields = ["value", "entity", "attribute"]

    def get_value(self, obj):
        return obj.value

    def create(self, validated_data):
        request_user = self.context["request"].user
        entity_data = validated_data.pop("entity")
        attribute_data = validated_data.pop("attribute")
        value_data = validated_data.pop("value")

        entity, _ = Entity.objects.get_or_create(
            name=entity_data["name"], user=request_user
        )
        attribute, _ = Attribute.objects.get_or_create(
            name=attribute_data["name"],
            defaults={"attribute_type": attribute_data["attribute_type"]},
        )

        field_name = {
            "text": "text_value",
            "integer": "integer_value",
            "float": "float_value",
            "date": "date_value",
            "boolean": "boolean_value",
        }.get(attribute.attribute_type)

        if not field_name:
            raise serializers.ValidationError({"value": "Invalid attribute type."})

        return Value.objects.create(
            entity=entity, attribute=attribute, **{field_name: value_data}
        )
