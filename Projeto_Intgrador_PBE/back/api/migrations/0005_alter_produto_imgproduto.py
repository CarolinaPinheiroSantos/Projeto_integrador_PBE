# Generated by Django 5.1 on 2024-11-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_produto_imgproduto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imgProduto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
