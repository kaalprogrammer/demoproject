# Generated by Django 3.2.7 on 2022-02-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
