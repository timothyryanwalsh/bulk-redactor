# Generated by Django 2.0.6 on 2018-06-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180613_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='besession',
            name='extracted_transfer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
