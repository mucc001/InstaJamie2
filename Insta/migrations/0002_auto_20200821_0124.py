# Generated by Django 3.1 on 2020-08-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instauser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
