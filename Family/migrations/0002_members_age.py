# Generated by Django 4.0.6 on 2022-07-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
