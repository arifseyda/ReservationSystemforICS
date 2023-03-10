# Generated by Django 3.1.1 on 2020-10-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervasyon', '0021_auto_20201009_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='updated_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Power System'), (1, 'Water System'), (2, 'Blade')], default=0),
        ),
    ]
