# Generated by Django 2.0.5 on 2019-03-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0006_auto_20190315_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletinboard',
            name='secret',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
