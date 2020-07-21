# Generated by Django 3.0.8 on 2020-07-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_tutorial_tutorialcategory_tutorialseries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
    ]