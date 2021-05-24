# Generated by Django 3.1.7 on 2021-05-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0007_auto_20210523_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='fuser',
            name='user_id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='fuser',
            name='user_name',
            field=models.CharField(max_length=256, verbose_name='이름'),
        ),
    ]