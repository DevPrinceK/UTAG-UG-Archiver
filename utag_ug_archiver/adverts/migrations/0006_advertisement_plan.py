# Generated by Django 4.2.6 on 2024-05-09 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_advertisement_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adverts.advertplan'),
        ),
    ]
