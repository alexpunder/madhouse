# Generated by Django 5.1.2 on 2024-11-01 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maindata',
            name='service',
        ),
        migrations.RemoveField(
            model_name='maindata',
            name='service_example',
        ),
        migrations.AddField(
            model_name='service',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maindata'),
        ),
        migrations.AddField(
            model_name='serviceexample',
            name='service_example',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maindata'),
        ),
    ]
