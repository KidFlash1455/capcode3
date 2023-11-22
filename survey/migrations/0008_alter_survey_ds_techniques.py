# Generated by Django 4.2.7 on 2023-11-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_survey_ds_techniques'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='ds_techniques',
            field=models.CharField(default='', max_length=200, verbose_name="Data Science Methods and Analytical Techniques (Pick the most prevalent methodology or techniques you teach or use in your data science research. Select 'Other' to list others you frequently use in the comment box. This will become a filterable list on a future version of the faculty web-site. Limit to 5-7.)"),
        ),
    ]