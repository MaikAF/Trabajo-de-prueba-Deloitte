# Generated by Django 4.2.6 on 2023-11-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
