# Generated by Django 4.0.3 on 2022-03-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwd', '0007_alter_generator_validity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='generator',
            name='caracteres',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='generator',
            name='chiffres',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='generator',
            name='lettres',
            field=models.BooleanField(default=True),
        ),
    ]