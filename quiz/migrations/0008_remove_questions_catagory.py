# Generated by Django 3.0.8 on 2020-07-19 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_questions_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='catagory',
        ),
    ]