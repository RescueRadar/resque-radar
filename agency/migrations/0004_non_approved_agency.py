# Generated by Django 4.2.5 on 2023-09-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_collaborationrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='non_approved_agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location_lat', models.FloatField(default=0.0)),
                ('location_long', models.FloatField(default=0.0)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('manpower', models.IntegerField()),
                ('volunteers', models.IntegerField()),
                ('category_of_calamity', models.CharField(max_length=50)),
                ('category_of_service', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'non_approved_agencies',
            },
        ),
    ]
