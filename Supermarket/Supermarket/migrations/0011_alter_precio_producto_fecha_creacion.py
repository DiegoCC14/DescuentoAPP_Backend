# Generated by Django 5.0.6 on 2024-08-09 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermarket', '0010_alter_precio_producto_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio_producto',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 18, 37, 48, 125411)),
        ),
    ]
