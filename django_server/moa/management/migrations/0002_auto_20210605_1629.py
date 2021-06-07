# Generated by Django 3.1.7 on 2021-06-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='longtitude',
        ),
        migrations.AddField(
            model_name='manager',
            name='longitude',
            field=models.CharField(default='127.123', max_length=20, verbose_name='경도'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manager',
            name='latitude',
            field=models.CharField(max_length=20, verbose_name='위도'),
        ),
    ]