# Generated by Django 4.0.3 on 2022-03-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smugfolioapi', '0003_remove_images_file_name_remove_images_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smug_users',
            name='business_name',
            field=models.CharField(default='Going-To-The-Sun-Photography', max_length=256),
        ),
    ]
