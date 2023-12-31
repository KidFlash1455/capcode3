# Generated by Django 4.2.7 on 2023-11-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_survey_first_name_alter_survey_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='status',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=100, verbose_name='What is your status at the Marquette or UW-Milwaukee?'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='suffix',
            field=models.CharField(default='Default', max_length=100, verbose_name='Full Name including degrees/designations to be listed on web-site and directory:'),
        ),
    ]
