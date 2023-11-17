# Generated by Django 4.2.7 on 2023-11-17 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Default', max_length=100)),
                ('last_name', models.CharField(default='Default', max_length=100)),
                ('suffix', models.CharField(default='Default', max_length=100)),
                ('email', models.EmailField(default='Default@default.com', max_length=254)),
                ('status', models.CharField(default='Default', max_length=500)),
                ('status_desc', models.TextField(default='Default', max_length=500)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
