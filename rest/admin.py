from django.contrib import admin
from rest.models.eav_typed_column import Entity, Attribute, Value
# Register your models here.


admin.site.register(Entity)
admin.site.register(Attribute)
admin.site.register(Value)
