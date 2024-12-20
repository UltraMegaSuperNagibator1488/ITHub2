# Generated by Django 5.0.6 on 2024-10-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='Category')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='is_used_in_exam',
            field=models.BooleanField(default=False, verbose_name='Is used in exam'),
        ),
    ]
