# Generated by Django 3.2.19 on 2023-07-03 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_user_name_usermaster_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='activation_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='expiry_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
