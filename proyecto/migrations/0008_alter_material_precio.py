# Generated by Django 3.2.2 on 2022-10-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_alter_material_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='precio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
