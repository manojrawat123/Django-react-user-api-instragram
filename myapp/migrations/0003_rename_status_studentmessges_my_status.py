# Generated by Django 4.0.3 on 2023-04-27 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_studentmessges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmessges',
            old_name='status',
            new_name='my_status',
        ),
    ]