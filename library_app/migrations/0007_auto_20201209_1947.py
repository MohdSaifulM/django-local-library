# Generated by Django 3.1.4 on 2020-12-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_auto_20201209_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
