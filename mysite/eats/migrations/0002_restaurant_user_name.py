# Generated by Django 2.1.5 on 2019-01-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='user_name',
            field=models.CharField(default='charField', max_length=30),
        ),
    ]
