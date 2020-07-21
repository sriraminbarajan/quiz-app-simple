# Generated by Django 3.0.8 on 2020-07-19 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200719_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['category'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.RemoveField(
            model_name='questions',
            name='catagory',
        ),
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Category'),
        ),
    ]