# Generated by Django 2.2 on 2020-04-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sympthon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_title', models.CharField(max_length=200)),
                ('persian_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_title', models.CharField(max_length=200)),
                ('persian_title', models.CharField(max_length=200)),
                ('sympthons', models.ManyToManyField(to='medical.Sympthon')),
            ],
        ),
    ]
