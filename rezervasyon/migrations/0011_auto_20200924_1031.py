# Generated by Django 3.1.1 on 2020-09-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0010_remove_reservation_deneme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reserved_end_date',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserved_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
