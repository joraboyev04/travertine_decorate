# Generated by Django 4.0.3 on 2022-05-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='products')),
                ('narx', models.CharField(max_length=200)),
            ],
        ),
    ]
