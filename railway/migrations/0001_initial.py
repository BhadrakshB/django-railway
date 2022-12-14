# Generated by Django 4.0.3 on 2022-07-28 05:19

from django.db import migrations, models
import railway.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boarding_place', models.CharField(max_length=100)),
                ('destination_place', models.CharField(max_length=100)),
                ('date_of_travel', models.DateTimeField()),
                ('passenger_names', models.CharField(max_length=100)),
                ('passenger_age', models.IntegerField(verbose_name=2)),
                ('passenger_senior_citizen', models.BooleanField()),
                ('passenger_berth_preference', models.CharField(choices=[(railway.models.Berth_Preferences['L'], 'Lower'), (railway.models.Berth_Preferences['M'], 'Middle'), (railway.models.Berth_Preferences['U'], 'Upper')], max_length=1)),
            ],
        ),
    ]
