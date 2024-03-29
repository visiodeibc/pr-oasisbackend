# Generated by Django 2.2.5 on 2019-10-14 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191013_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptions',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='descriptions', serialize=False, to='api.Places'),
        ),
        migrations.AlterField(
            model_name='enaddress',
            name='descriptions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='enAddress', serialize=False, to='api.Descriptions'),
        ),
        migrations.AlterField(
            model_name='hkaddress',
            name='descriptions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='hkAddress', serialize=False, to='api.Descriptions'),
        ),
    ]
