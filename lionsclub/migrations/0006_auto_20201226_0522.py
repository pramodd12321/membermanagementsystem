# Generated by Django 3.1.4 on 2020-12-26 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lionsclub', '0005_auto_20201219_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='user',
            new_name='owner',
        ),
    ]