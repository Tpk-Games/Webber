# Generated by Django 2.1.4 on 2019-01-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to='post/'),
        ),
    ]
