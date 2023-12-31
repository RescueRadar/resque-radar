# Generated by Django 4.2.5 on 2023-09-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_alter_agency_about_alter_agency_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='victims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('type_incident', models.CharField(max_length=100)),
                ('num_of_people', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='agency',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='agency',
            name='email',
            field=models.EmailField(max_length=500),
        ),
        migrations.AlterField(
            model_name='agency',
            name='locality',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='agency',
            name='state',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='agency',
            name='website',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='email',
            field=models.EmailField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='locality',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='state',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='non_approved_agency',
            name='website',
            field=models.CharField(max_length=500),
        ),
    ]
