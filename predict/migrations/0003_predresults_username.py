# Generated by Django 4.0.3 on 2022-05-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_remove_predresults_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='predresults',
            name='username',
            field=models.CharField(default='admin', max_length=60),
        ),
    ]
