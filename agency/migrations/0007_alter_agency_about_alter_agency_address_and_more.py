# Generated by Django 4.2.5 on 2023-09-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0006_alter_agency_user_alter_non_approved_agency_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='agency',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]
