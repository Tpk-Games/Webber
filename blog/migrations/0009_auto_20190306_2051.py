# Generated by Django 2.1.5 on 2019-03-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190201_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.IntegerField(choices=[(1, 'state_choices_1'), (2, 'state_choices_2'), (3, 'state_choices_3')], default=1),
        ),
    ]