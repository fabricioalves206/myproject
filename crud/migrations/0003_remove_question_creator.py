# Generated by Django 4.2.4 on 2023-08-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_question_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
    ]
