# Generated by Django 3.0.8 on 2020-07-20 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_questions_catagory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ('-catagory',)},
        ),
    ]
