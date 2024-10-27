# Generated by Django 5.0.6 on 2024-09-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ege_num', models.IntegerField(verbose_name='EGE Number')),
                ('desc', models.TextField(verbose_name='Description')),
                ('ege_data', models.CharField(max_length=4, null=True, verbose_name='First appeared in EGE')),
                ('is_used_in_exam', models.BooleanField(default=False, verbose_name='is used in exam')),
            ],
        ),
    ]