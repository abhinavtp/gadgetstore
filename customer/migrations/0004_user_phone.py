# Generated by Django 4.1.5 on 2023-01-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(default='9897867567'),
            preserve_default=False,
        ),
    ]
