# Generated by Django 4.2.6 on 2024-07-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_user_created_at_user_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_bulk_creation',
            field=models.BooleanField(default=False),
        ),
    ]