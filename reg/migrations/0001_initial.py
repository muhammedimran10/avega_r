# Generated by Django 4.1.5 on 2023-01-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phno', models.CharField(max_length=10)),
                ('clg_name', models.CharField(max_length=30)),
                ('corse_name', models.CharField(max_length=10)),
            ],
        ),
    ]