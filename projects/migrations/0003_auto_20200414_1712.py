# Generated by Django 3.0.5 on 2020-04-15 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200414_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='work_in_progress',
            field=models.CharField(choices=[('Ideation Phase', 'ID8'), ('Development Phase', 'DPP'), ('Testing Phase', 'TP'), ('Finished', 'FIN')], max_length=20),
        ),
    ]
