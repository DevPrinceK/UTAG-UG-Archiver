# Generated by Django 4.2.6 on 2024-03-07 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_rename_message_document_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='comment',
            new_name='message',
        ),
    ]
