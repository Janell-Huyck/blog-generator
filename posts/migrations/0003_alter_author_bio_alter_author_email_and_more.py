# Generated by Django 4.2.1 on 2023-05-22 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_author_home_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
