# Generated by Django 3.2 on 2021-05-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210511_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
