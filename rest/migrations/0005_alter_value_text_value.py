# Generated by Django 5.1.6 on 2025-02-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest", "0004_alter_value_boolean_value_alter_value_date_value_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="value",
            name="text_value",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
