# Generated by Django 3.2.19 on 2023-07-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20230707_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('prod_id', models.IntegerField()),
            ],
        ),
    ]
