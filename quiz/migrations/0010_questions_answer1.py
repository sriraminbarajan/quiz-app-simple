# Generated by Django 3.0.8 on 2020-07-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20200720_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answer1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
