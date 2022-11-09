# Generated by Django 3.2.13 on 2022-04-19 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(5.0)])),
                ('max_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(12)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]