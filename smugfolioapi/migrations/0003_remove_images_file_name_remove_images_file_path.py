# Generated by Django 4.0.3 on 2022-03-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugfolioapi', '0002_rename_smug_user_id_images_smug_user_images_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='images',
            name='file_path',
        ),
    ]
