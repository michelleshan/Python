# Generated by Django 2.2 on 2020-03-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]