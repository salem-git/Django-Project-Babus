# Generated by Django 3.0 on 2020-02-02 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0003_auto_20200202_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='description',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='is_reserved',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='mile',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='name',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='timetaken',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='user',
        ),
    ]