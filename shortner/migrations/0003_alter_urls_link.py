# Generated by Django 4.2.5 on 2023-10-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_alter_urls_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='link',
            field=models.CharField(max_length=16300),
        ),
    ]
