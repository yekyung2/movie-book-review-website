# Generated by Django 2.2.5 on 2021-02-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210217_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('eng', 'eng'), ('kr', 'kr')], max_length=10, null=True),
        ),
    ]
