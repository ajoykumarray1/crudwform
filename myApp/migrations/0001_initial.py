# Generated by Django 4.2.7 on 2023-11-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_pic', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(max_length=30)),
            ],
        ),
    ]
