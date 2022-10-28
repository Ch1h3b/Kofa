# Generated by Django 4.0.6 on 2022-07-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kufa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
                ('adress', models.CharField(max_length=300)),
                ('items', models.CharField(max_length=500)),
                ('taken', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=32)),
            ],
        ),
    ]