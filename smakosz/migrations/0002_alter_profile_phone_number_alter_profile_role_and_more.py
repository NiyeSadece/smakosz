# Generated by Django 4.2.7 on 2023-11-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smakosz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('1', 'Customer'), ('2', 'Staff'), ('3', 'Administrator')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.CharField(max_length=2),
        ),
    ]
