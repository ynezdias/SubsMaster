# Generated by Django 3.2.19 on 2023-07-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_usermaster_activation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='last_login',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
