# Generated by Django 2.0.2 on 2018-03-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_auto_20180326_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='episodes',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
