# Generated by Django 2.0.6 on 2018-06-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_redactedset'),
    ]

    operations = [
        migrations.AddField(
            model_name='redactedset',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
