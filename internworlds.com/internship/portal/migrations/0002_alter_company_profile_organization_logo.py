# Generated by Django 3.2 on 2021-12-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='organization_logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]