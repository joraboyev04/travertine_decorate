# Generated by Django 4.0.3 on 2022-05-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_pictures_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]