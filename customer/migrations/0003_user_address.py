# Generated by Django 4.1.5 on 2023-01-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Mukkam', max_length=100),
            preserve_default=False,
        ),
    ]