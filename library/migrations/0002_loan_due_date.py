# Generated by Django 4.2 on 2025-03-19 17:52

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateField(default=library.models.default_due_date),
        ),
    ]
