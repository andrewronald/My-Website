# Generated by Django 3.0.5 on 2020-04-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_text',
            field=models.TextField(),
        ),
    ]
