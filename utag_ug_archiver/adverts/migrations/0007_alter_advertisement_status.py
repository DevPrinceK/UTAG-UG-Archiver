# Generated by Django 4.2.6 on 2024-05-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_advertisement_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('EXPIRED', 'Expired')], default='DRAFT', max_length=20),
        ),
    ]