# Generated by Django 2.0.5 on 2018-05-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0002_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('handle', models.CharField(max_length=50)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontEnd.Player')),
            ],
        ),
    ]
