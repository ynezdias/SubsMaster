# Generated by Django 3.2.19 on 2023-06-20 21:01

from django.db import migrations, models
import django.utils.timezone

def create_dummy_users(apps, schema_editor):
    User = apps.get_model('dashboard_app', 'User')

    # Create and save dummy users
    User.objects.create(username='user1', activation_date='2023-05-01', expiry_date='2023-06-01')
    User.objects.create(username='user2', activation_date='2023-05-02', expiry_date='2023-06-02')
    User.objects.create(username='user3', activation_date='2023-05-03', expiry_date='2023-06-03')    


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='end_date',
        ),
        
        migrations.AddField(
            model_name='usermaster',
            name='activation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usermaster',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
           
        migrations.RunPython(create_dummy_users),
    ]


