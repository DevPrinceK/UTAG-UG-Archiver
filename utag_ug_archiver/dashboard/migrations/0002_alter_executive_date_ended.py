# Generated by Django 4.2.6 on 2023-10-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='date_ended',
            field=models.DateField(blank=True, null=True),
        ),
    ]
