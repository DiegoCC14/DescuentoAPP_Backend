# Generated by Django 5.0.6 on 2024-08-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supermarket', '0002_remove_negocios_path_imagen_negocios_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocios',
            name='imagen',
            field=models.ImageField(default='statics/imagen/negocios/base_supermarket.jpg', upload_to='statics/imagen/negocios/'),
        ),
    ]
