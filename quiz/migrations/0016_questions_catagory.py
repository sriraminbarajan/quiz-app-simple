# Generated by Django 3.0.8 on 2020-07-20 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='catagory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quiz.Catagory'),
            preserve_default=False,
        ),
    ]
