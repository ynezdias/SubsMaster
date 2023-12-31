# Generated by Django 4.2.2 on 2023-06-19 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usermaster',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),


        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('act_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.usermaster')),
            ],
        ),
    ]


