# Generated by Django 3.0.4 on 2020-03-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0003_auto_20200327_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='uploaded_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
