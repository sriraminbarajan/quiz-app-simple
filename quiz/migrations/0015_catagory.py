# Generated by Django 3.0.8 on 2020-07-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quiz_category', models.CharField(max_length=50)),
            ],
        ),
    ]
