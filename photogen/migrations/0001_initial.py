# Generated by Django 5.0 on 2024-02-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_num', models.PositiveSmallIntegerField()),
                ('image_url', models.FileField(upload_to='')),
            ],
        ),
    ]