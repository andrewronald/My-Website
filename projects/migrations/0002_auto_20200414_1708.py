# Generated by Django 3.0.5 on 2020-04-15 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='work_in_progress',
            field=models.CharField(choices=[('ID8', 'Ideation Phase'), ('DPP', 'Development Phase'), ('TP', 'Testing Phase'), ('FIN', 'Finished')], max_length=8),
        ),
    ]
