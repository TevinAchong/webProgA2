# Generated by Django 2.0.2 on 2018-04-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0007_auto_20180330_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='imageUrl',
            field=models.CharField(default='http://www.pixedelic.com/themes/geode/demo/wp-content/uploads/sites/4/2014/04/placeholder.png', max_length=500),
            preserve_default=False,
        ),
    ]
