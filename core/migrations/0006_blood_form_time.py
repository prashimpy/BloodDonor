# Generated by Django 3.2.12 on 2022-07-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_blood_form_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_form',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
