# Generated by Django 3.0.8 on 2020-07-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_delete_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('answer1', models.CharField(max_length=100)),
            ],
        ),
    ]
