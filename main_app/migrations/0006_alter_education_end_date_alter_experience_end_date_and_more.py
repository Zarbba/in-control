# Generated by Django 5.1.4 on 2025-01-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_education_end_date_alter_experience_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='headline',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, choices=[('MR', 'Mr'), ('MISS', 'Miss'), ('MRS', 'Mrs'), ('MX', 'Mx'), ('MS', 'Ms'), ('O', 'Other')], default='MR', max_length=4),
        ),
    ]