# Generated by Django 5.0 on 2024-02-17 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogen', '0006_delete_randomimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionzip',
            name='id',
        ),
        migrations.AlterField(
            model_name='sessionzip',
            name='session_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
    ]
