# Generated by Django 2.0.5 on 2018-05-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0003_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]