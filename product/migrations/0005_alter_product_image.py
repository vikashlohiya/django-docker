# Generated by Django 4.2.3 on 2023-07-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='product/'),
        ),
    ]