# Generated by Django 3.0.5 on 2021-01-28 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210127_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Coding', 'Codings')], max_length=255),
        ),
    ]
