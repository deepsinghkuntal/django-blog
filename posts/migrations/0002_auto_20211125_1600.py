# Generated by Django 3.2.8 on 2021-11-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message_html',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
