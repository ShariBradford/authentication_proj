# Generated by Django 2.2 on 2020-07-12 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
