# Generated by Django 3.2 on 2021-05-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='john doe', max_length=99),
            preserve_default=False,
        ),
    ]