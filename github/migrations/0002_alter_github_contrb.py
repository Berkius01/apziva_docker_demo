# Generated by Django 4.1.1 on 2022-09-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='contrb',
            field=models.CharField(max_length=100),
        ),
    ]
