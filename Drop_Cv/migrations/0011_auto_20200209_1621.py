# Generated by Django 2.2.8 on 2020-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drop_Cv', '0010_auto_20200204_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]