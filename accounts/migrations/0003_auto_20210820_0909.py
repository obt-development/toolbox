# Generated by Django 3.2.6 on 2021-08-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210820_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='street_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='street number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='street',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='street'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='town',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='town'),
        ),
    ]
