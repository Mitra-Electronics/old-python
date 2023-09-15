# Generated by Django 2.1.5 on 2021-01-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_slug', models.SlugField(unique=True)),
                ('item_title', models.CharField(max_length=255)),
                ('item_description', models.CharField(max_length=2000)),
                ('item_date', models.DateField()),
            ],
        ),
    ]