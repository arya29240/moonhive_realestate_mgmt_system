# Generated by Django 4.2.7 on 2024-01-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0003_tenant_rentaldetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
