# Generated by Django 2.2.5 on 2019-10-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilityId', models.CharField(max_length=50)),
                ('facilityType', models.CharField(max_length=60)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('phone', models.CharField(max_length=15)),
                ('accessibility', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
