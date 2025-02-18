# Generated by Django 5.1.6 on 2025-02-18 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('column_type', models.CharField(choices=[('BooleanField', 'BooleanField'), ('CharField', 'CharField'), ('DateField', 'DateField'), ('DecimalField', 'DecimalField'), ('DurationField', 'DurationField'), ('FilePathField', 'FilePathField'), ('FloatField', 'FloatField'), ('IntegerField', 'IntegerField'), ('IPAddressField', 'IPAddressField'), ('GenericIPAddressField', 'GenericIPAddressField'), ('TextField', 'TextField'), ('TimeField', 'TimeField'), ('BinaryField', 'BinaryField'), ('UUIDField', 'UUIDField'), ('JSONField', 'JSONField'), ('FileField', 'FileField'), ('GeneratedField', 'GeneratedField'), ('RelatedField', 'RelatedField')], max_length=50)),
                ('is_nullable', models.BooleanField(default=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='rest.table')),
            ],
        ),
    ]
