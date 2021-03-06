# Generated by Django 3.0.2 on 2020-01-27 23:52

from django.db import migrations
import django.db.models.deletion
import officials.models


class Migration(migrations.Migration):

    dependencies = [
        ('officials', '0005_publicofficial_position_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossbyreport',
            name='SubAgencyNo',
            field=officials.models.CFBZeroForeignKeyField(on_delete=django.db.models.deletion.CASCADE, to='officials.SubAgency'),
        ),
        migrations.AlterField(
            model_name='position',
            name='SubAgencyNo',
            field=officials.models.CFBZeroForeignKeyField(on_delete=django.db.models.deletion.CASCADE, to='officials.SubAgency'),
        ),
    ]
