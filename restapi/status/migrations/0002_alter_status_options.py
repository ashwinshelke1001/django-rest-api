# Generated by Django 3.2 on 2021-10-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status post', 'verbose_name_plural': 'status posts'},
        ),
    ]
