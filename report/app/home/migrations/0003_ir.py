# Generated by Django 2.2.7 on 2019-12-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191220_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='IR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('university', models.TextField(max_length=50)),
            ],
        ),
    ]
