# Generated by Django 2.2.4 on 2019-08-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_delete_votecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_reporter',
            field=models.BooleanField(default=False),
        ),
    ]
