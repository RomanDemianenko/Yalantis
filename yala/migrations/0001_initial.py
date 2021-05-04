# Generated by Django 3.2 on 2021-05-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('num_lectures', models.PositiveIntegerField()),
            ],
        ),
    ]
