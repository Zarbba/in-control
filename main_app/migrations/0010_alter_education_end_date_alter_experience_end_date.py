# Generated by Django 5.1.5 on 2025-01-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]