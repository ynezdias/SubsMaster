# Generated by Django 3.2.19 on 2023-07-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_usermaster_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
