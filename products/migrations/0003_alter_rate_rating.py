# Generated by Django 4.2.7 on 2023-12-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]