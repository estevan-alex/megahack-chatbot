# Generated by Django 2.2.3 on 2020-05-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_product_id_amazon'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link_amazon',
            field=models.CharField(default='AAAA', max_length=300),
            preserve_default=False,
        ),
    ]
