# Generated by Django 5.1.5 on 2025-01-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_education_end_date_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]